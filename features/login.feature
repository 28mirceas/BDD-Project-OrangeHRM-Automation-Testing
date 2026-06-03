Feature: Login OrangeHRM

  Background: Open the OrangeHRM page
    Given Navigate to OrangeHRM page


  @login
  Scenario: Login as admin user with valid credentials
    When Enter "Admin" in the username input field
    And Enter "admin123" in the password input field
    And Click the Login button
    Then The url of the new page is "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    And The header text of the new page is "Dashboard"



  @negativeLogin
  Scenario: Login as admin  user with invalid credentials
    When Enter "Admin" in the username input field
    And Enter "admin1234" in the password input field
    And Click the Login button
    Then The error text for the invalid password is "Invalid credentials"
    And The user remains on the Login page


