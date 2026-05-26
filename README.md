# BDD Project – OrangeHRM Automation Testing

## Project Description
This project represents a **BDD (Behavior Driven Development)** automated test suite for the **OrangeHRM** web application, using **Python, Behave, and Selenium WebDriver**.

The purpose of this project is to validate the main functionalities of the OrangeHRM application, such as:
- user authentication
- employee management (add, search, edit)
- dashboard functionality verification

The tested application is the OrangeHRM demo version:  
https://opensource-demo.orangehrmlive.com

---

## Test Types
- ✅ Automated functional tests
- ✅ BDD tests (Gherkin – Given / When / Then)
- ❌ Negative tests (login with invalid credentials)

---

## Technologies Used
- **Python**
- **Behave**
- **Selenium WebDriver**
- **Page Object Model (POM)**
- **Gherkin**
- **ChromeDriver**

---

## Project Structure
```
BDD-Project-OrangeHRM/
├── features/
│   ├── login.feature
│   ├── dashboard.feature
│
│── steps/
│       ├── login_steps.py
│       └── dashboard_steps.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── browser.py
├── environment.py
├── requirements.txt
└── README.md
```


---

## Test Execution
```bash
behave
```

---

## Author
Project created for educational purposes, focused on BDD automated testing.
