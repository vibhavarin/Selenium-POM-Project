# Selenium PyTest Automation Project

A robust and scalable web test automation framework built using Python, Selenium WebDriver, and the **Page Object Model (POM)** design pattern. This project demonstrates clean automation practices, complete separation of test logic from UI elements, and a highly maintainable test suite powered by PyTest.

## 🚀 Features
* **Page Object Model (POM):** Enhances test maintenance and reduces code duplication.
* **PyTest Framework:** Leverages powerful fixtures for setup/teardown and parallel test execution capabilities.
* **Separation of Concerns:** Clean split between page actions, locators, and test scripts.
* **Robust Locators:** Optimized element identification using reliable IDs, CSS selectors, and XPaths.

## 🛠️ Tech Stack & Prerequisites
Before running the tests, ensure you have the following installed:
* **Python 3.x**
* **Google Chrome** (or your preferred browser)
* **WebDriver Manager** (handles ChromeDriver binaries automatically)

## 📁 Project Structure
```text
├── pages/              # Page classes containing web element locators and actions
│   ├── base_page.py    # Common wrapper functions for Selenium interactions
│   ├── login_page.py   # Locators and methods for the Login page
│   └── dashboard_page.py
├── tests/              # PyTest script files containing assertions
│   ├── conftest.py     # Global configurations and browser setup fixtures
│   └── test_login.py   # Actual login test scenarios
├── requirements.txt    # Project dependencies (Selenium, pytest, etc.)
└── README.md           # Documentation
```

## 💻 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Selenium-POM-Project
   ```

2. **Create and activate a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the test suite:**
   ```bash
   pytest
   ```
   *(Optional)* Run tests with a detailed console report:
   ```bash
   pytest -v -s
   ```

## 📊 Sample Test Scenarios
* **Valid Login:** Verifies successful user login with correct credentials.
* **Invalid Login:** Validates error handling and alert messages for incorrect inputs.
