# BDD OrangeHRM Project – Test Automation with Behave & Selenium
![CI](https://github.com/28mirceas/BDD-Project-OrangeHRM-Automation-Testing/actions/workflows/behave-tests.yml/badge.svg)

## Description

This project contains automated UI tests for the OrangeHRM Demo application using Behavior-Driven Development (BDD) with Behave and Selenium WebDriver.

The framework follows the Page Object Model (POM) design pattern to ensure maintainability, readability, and scalability.

Application under test:

https://opensource-demo.orangehrmlive.com/

---

## Technologies Used

* Python 3
* Behave (BDD Framework)
* Selenium WebDriver
* Page Object Model (POM)
* Chrome WebDriver
* Git & GitHub

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/28mirceas/BDD-Project-OrangeHRM-Automation-Testing.git
cd BDD-Project-OrangeHRM-Automation-Testing
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure WebDriver

Make sure that Google Chrome and the appropriate ChromeDriver version are installed.

---

## Running the Tests

Run all scenarios:

```bash
behave
```

Run with verbose output:

```bash
behave -v
```

Run scenarios by tag:

```bash
behave --tags=login
```

```bash
behave --tags=openEmployeeListPage
```

```bash
behave --tags=addEmployee
```

```bash
behave --tags=negativeEmployee
```

```bash
behave --tags=logoutUser
```

---

## Included Test Scenarios

### Login

* Login as admin user with valid credentials
* Login with invalid credentials

### Dashboard Navigation

* Open Employee List page from the PIM menu

### Employee Management

* Add a new employee with valid data
* Add employee without mandatory fields

### Session Management

* Logout from OrangeHRM application

---

## Project Structure

```text
BDD-Project-OrangeHRM-Automation-Testing/
│
│ behave.ini
│ browser.py
│ environment.py
│ requirements.txt
│ README.md
│
├── features/
│   ├── login.feature
│   ├── dashboard.feature
│   └── employee.feature
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── employee_page.py
│
├── steps/
│   ├── login_steps.py
│   ├── dashboard_steps.py
│   └── employee_steps.py
│
└── __pycache__/
```

---

## Page Object Model

All pages are defined in the `pages/` folder.

Each page contains:

* element locators
* page actions
* reusable methods
* assertions

Implemented page objects:

* BasePage
* LoginPage
* DashboardPage
* EmployeePage

---

## Behave Configuration

The `behave.ini` file is used for:

* execution settings
* reporting options
* default Behave behavior

---

## Behave Hooks

The `environment.py` file contains:

* before_all
* before_scenario
* after_scenario
* after_all

These hooks handle:

* browser initialization
* browser cleanup
* test environment setup
* resource management

---

## Reports

The framework can be extended to generate:

* HTML reports
* JSON reports
* screenshots on failure

depending on the Behave configuration used.

---

## Design Pattern

This project follows the Page Object Model (POM) design pattern.

Benefits:

* Better code organization
* Improved maintainability
* Reusable page actions
* Easier test scalability

---

## Author

Mircea

GitHub Repository:

https://github.com/28mirceas/BDD-Project-OrangeHRM-Automation-Testing

---

## License

MIT License
