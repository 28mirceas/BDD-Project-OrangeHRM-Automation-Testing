Feature: Verify the functionality of the employeelist page


  @employeelist
  @addEmployee
  Scenario: Add a new employee with valid data
    When Click the Add Employee button
    And Enter "Ion" in the First Name input field
    And Enter "Popescu" in the Last Name input field
    And Enter employee id in the Employee Id input field
    And Click Save button
    Then The employee name in Personal Details page which is created is "Ion Popescu"


  @employeelist
  @negativeEmployee
  Scenario: Add employee without mandatory fields
    When Click the Add Employee button
    And Click Save button
    Then The error text for missing mandatory fields is "Required"


  @employeelist
  @logoutUser
  Scenario: Logout from OrangeHRM application
    When Click on the user dropdown menu
    And Click Logout button
    Then The user is redirected to page "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    And Login page is displayed




