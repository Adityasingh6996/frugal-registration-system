from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import time


def open_browser():
    """Open Chrome and load local index.html."""
    # Selenium 4+ will auto-manage ChromeDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    page_url = pathlib.Path(__file__).with_name("index.html").absolute().as_uri()
    driver.get(page_url)

    print("Page URL:", driver.current_url)
    print("Page Title:", driver.title)
    return driver


def fill_common_fields(driver, include_last_name=True):
    """Fill the form fields. Can skip last name (for negative test)."""
    wait = WebDriverWait(driver, 10)

    # First Name
    first = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
    first.clear()
    first.send_keys("Aaditya")

    # Last Name
    last = driver.find_element(By.ID, "lastName")
    last.clear()
    if include_last_name:
        last.send_keys("Singh")

    # Email
    email = driver.find_element(By.ID, "email")
    email.clear()
    email.send_keys("aaditya.example@gmail.com")

    # Phone
    phone = driver.find_element(By.ID, "phone")
    phone.clear()
    phone.send_keys("+919876543210")

    # Age
    age = driver.find_element(By.ID, "age")
    age.clear()
    age.send_keys("22")

    # Gender
    male_radio = driver.find_element(By.XPATH, "//input[@name='gender' and @value='Male']")
    male_radio.click()

    # Address
    address = driver.find_element(By.ID, "address")
    address.clear()
    address.send_keys("Sample address, Dehradun, India")

    # Country → India
    country = driver.find_element(By.ID, "country")
    country.click()
    country.find_element(By.XPATH, ".//option[text()='India']").click()
    time.sleep(0.5)

    # State → Uttarakhand
    state = driver.find_element(By.ID, "state")
    state.click()
    state.find_element(By.XPATH, ".//option[text()='Uttarakhand']").click()
    time.sleep(0.5)

    # City → Dehradun
    city = driver.find_element(By.ID, "city")
    city.click()
    city.find_element(By.XPATH, ".//option[text()='Dehradun']").click()

    # Password + Confirm Password
    password = driver.find_element(By.ID, "password")
    confirm = driver.find_element(By.ID, "confirmPassword")
    password.clear()
    confirm.clear()
    password.send_keys("Aa@12345")
    confirm.send_keys("Aa@12345")

    # Terms & Conditions
    terms = driver.find_element(By.ID, "terms")
    if not terms.is_selected():
        terms.click()


def flow_negative_missing_last_name():
    """
    Automation Flow A — Negative:
    - Skip last name
    - Force-enable submit (for automation)
    - Click and expect error + red highlight
    """
    print("\n=== Flow A: Negative (Missing Last Name) ===")
    driver = open_browser()
    wait = WebDriverWait(driver, 10)

    # Fill everything except last name
    fill_common_fields(driver, include_last_name=False)

    # Get the button (even if disabled)
    submit_btn = wait.until(EC.presence_of_element_located((By.ID, "submitBtn")))

    # For automation only: force-enable the button so we can click
    driver.execute_script("arguments[0].removeAttribute('disabled');", submit_btn)

    # Now click submit
    submit_btn.click()
    time.sleep(1)

    # Check top error alert
    top_error = driver.find_element(By.ID, "topError")
    if top_error.is_displayed():
        print("✅ Top error alert displayed.")
    else:
        print("❌ Top error alert NOT displayed.")

    # Check Last Name error
    last_group = driver.find_element(By.ID, "lastName").find_element(By.XPATH, "./..")
    error_span = last_group.find_element(By.CLASS_NAME, "error-text")
    if error_span.is_displayed():
        print("✅ Last Name error message displayed.")
    else:
        print("❌ Last Name error message MISSING.")

    driver.save_screenshot("error_state.png")
    print("📸 Screenshot saved: error_state.png")

    driver.quit()



def flow_positive_success():
    """
    Automation Flow B — Positive:
    - Fill all fields correctly
    - Submit
    - Expect success message + form reset
    """
    print("\n=== Flow B: Positive (Successful Submission) ===")
    driver = open_browser()
    wait = WebDriverWait(driver, 10)

    fill_common_fields(driver, include_last_name=True)

    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submitBtn")))
    submit_btn.click()
    time.sleep(1)

    top_success = driver.find_element(By.ID, "topSuccess")
    if top_success.is_displayed():
        print("✅ Success message displayed.")
    else:
        print("❌ Success message NOT displayed.")

    # After success, form resets → first name empty
    first_value = driver.find_element(By.ID, "firstName").get_attribute("value")
    if first_value == "":
        print("✅ Form fields reset after success.")
    else:
        print("❌ Form did not reset correctly.")

    driver.save_screenshot("success_state.png")
    print("📸 Screenshot saved: success_state.png")

    driver.quit()


def flow_logic_validation():
    """
    Automation Flow C — Logic:
    - Country change updates states
    - State change updates cities
    - Password + mismatch behaviour
    - Submit disabled when invalid & enabled when valid
    """
    print("\n=== Flow C: Logic Validation ===")
    driver = open_browser()
    wait = WebDriverWait(driver, 10)

    # Country → USA
    country = wait.until(EC.presence_of_element_located((By.ID, "country")))
    country.click()
    country.find_element(By.XPATH, ".//option[text()='USA']").click()
    time.sleep(0.5)
    state = driver.find_element(By.ID, "state")
    usa_states = [o.text for o in state.find_elements(By.TAG_NAME, "option")]
    print("States for USA:", usa_states)

    # Country → India
    country.click()
    country.find_element(By.XPATH, ".//option[text()='India']").click()
    time.sleep(0.5)
    state = driver.find_element(By.ID, "state")
    india_states = [o.text for o in state.find_elements(By.TAG_NAME, "option")]
    print("States for India:", india_states)

    if usa_states != india_states:
        print("✅ State dropdown updates when country changes.")
    else:
        print("❌ State dropdown did NOT update correctly.")

    # Password behaviour
    password = driver.find_element(By.ID, "password")
    confirm = driver.find_element(By.ID, "confirmPassword")
    submit_btn = driver.find_element(By.ID, "submitBtn")

    # Weak password
    password.clear()
    confirm.clear()
    password.send_keys("abc")
    time.sleep(0.5)
    print("Submit enabled with weak password? ->", submit_btn.is_enabled())

    # Mismatch password
    password.clear()
    confirm.clear()
    password.send_keys("Aa@12345")
    confirm.send_keys("wrong123")
    time.sleep(0.5)
    print("Submit enabled when passwords mismatch? ->", submit_btn.is_enabled())

    # Now fill everything valid (re-use helper)
    fill_common_fields(driver, include_last_name=True)
    time.sleep(0.5)
    print("Submit enabled after valid data? ->", submit_btn.is_enabled())

    driver.save_screenshot("logic_state.png")
    print("📸 Screenshot saved: logic_state.png")

    driver.quit()


if __name__ == "__main__":
    flow_negative_missing_last_name()
    flow_positive_success()
    flow_logic_validation()
    print("\n✅ All three flows completed.")
