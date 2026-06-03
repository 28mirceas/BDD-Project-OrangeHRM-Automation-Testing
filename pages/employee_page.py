from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time

class EmployeeListPage(BasePage):

    BUTTON_ADD_EMPLOYEE = (By.XPATH,"//a[contains(@href,'addEmployee')]")
    BUTTON_EMPLOYEE_LIST = (By.XPATH, "//a[text() = 'Employee List']")
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMPLOYEE_ID = (By.XPATH, "//label[normalize-space()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message')]")
    LOADER = (By.CLASS_NAME, "oxd-form-loader")
    BUTTON_SAVE = (By.XPATH, "//button[@type='submit']")
    PERSONAL_PAGE_NAME = (By.XPATH, "//div[contains(@class,'orangehrm-edit-employee-name')]//h6")

    USER_DROPDOWN_MENU = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LINK_LOGOUT = (By.XPATH, "//a[text()='Logout']")
    LOGIN_TITLE = (By.XPATH, "//h5[text()='Login']")


    def __init__(self, driver):
        super().__init__(driver)


    def click_add_employee(self):
        self.click(self.BUTTON_ADD_EMPLOYEE)


    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)


    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)


    def set_employee_id(self):
        employee_id = str(int(time.time()))

        field = self.find(self.EMPLOYEE_ID)
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(employee_id)


    def wait_for_loader_to_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.LOADER)
        )


    def click_save(self):
        self.wait_for_loader_to_disappear()
        self.click(self.BUTTON_SAVE)



    #searchEmployee Scenario
    def click_employee_list(self):
        self.click(self.BUTTON_EMPLOYEE_LIST)

        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'oxd-table-filter')]")
            )
        )
        time.sleep(0.5)



    def click_user_dropdown_menu(self):
        self.click(self.USER_DROPDOWN_MENU)
        self.wait.until(
            EC.visibility_of_element_located(self.LINK_LOGOUT)
        )


    def click_logout_button(self):
        self.click(self.LINK_LOGOUT)


    def verify_login_page_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_TITLE))



