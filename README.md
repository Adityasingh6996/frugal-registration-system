🚀 Intelligent Registration System – Selenium Automation Project

This project is part of the Frugal Testing – Software Engineer Assignment.
It demonstrates a complete front-end registration form and automated test flows using Selenium + Python.

📌 Project Overview

This project includes:

✅ 1. Registration Form (index.html)

A fully responsive, validation-enabled registration form built using HTML, CSS, and JavaScript.

Features:

Required field validation

Dynamic Country → State → City population

Password strength meter

Email & phone validation

Submit button enable/disable logic

Success & error alert messages

✅ 2. Selenium Automation (test_registration.py)

Three automated flows were developed:

🔴 Flow A – Negative Test

Missing Last Name

Submit button forced for testing

Ensure proper error message & red highlight

Screenshot saved: error_state.png

🟢 Flow B – Positive Test

All fields filled correctly

Successful submission message displayed

Form resets after success

Screenshot saved: success_state.png

🔵 Flow C – Logic Validation

Country → State → City dropdown mapping

Password validation & mismatch logic

Submit enabled only when all conditions are met

Screenshot saved: logic_state.png

Screenshots for each flow are automatically captured by Selenium.

frugal_registration_system/
│
├── index.html                 # Registration UI
├── test_registration.py       # Selenium automation script
│
├── error_state.png            # Negative flow screenshot
├── success_state.png          # Positive flow screenshot
├── logic_state.png            # Logic validation screenshot
│
└── frugal_registration_demo.mp4   # Full automation video (optional)

🧪 Tech Stack
Frontend

HTML5

CSS3

JavaScript (vanilla)

Automation

Python (Selenium)

Selenium WebDriver

Chrome Browser + Selenium Manager

WebDriverWait + Explicit Waits
▶️ How to Run the Automation Script
1️⃣ Install Dependencies
py -m pip install selenium


Selenium Manager automatically handles ChromeDriver.

2️⃣ Run the Script

Make sure index.html and test_registration.py are in the same folder.

Run:

py test_registration.py


Chrome will open three times, each for one flow.
📷 Screenshots
Flow	Screenshot
Negative (Missing Last Name)	error_state.png
Positive (Success Form Submission)	success_state.png
Logic Validation (Dropdowns, Password Rules)	logic_state.png

🎥 Demo Video

A full automation run is recorded and saved as:

frugal_registration_demo.mp4
Live Assets (Google Drive)

Drive link with all screenshots, code files, and video:
👉 [https://drive.google.com/drive/folders/1TwOoWtHBJ4gCO8V0nnGtBXrzZccQoO05?usp=sharing]
👨‍💻 Developer

Aaditya Singh
B.Tech CSE Student
Skilled in Python, Automation, Web Dev, and Testing



