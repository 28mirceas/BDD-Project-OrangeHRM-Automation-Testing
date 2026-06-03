from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def find_multiple(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))


    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)


    def select_item_by_text(self, locator, text):
        dropdown_element = self.wait.until(EC.element_to_be_clickable(locator))
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(text)


    def select_custom_dropdown(self, dropdown_locator, option_text):
        wait = WebDriverWait(self.driver, 10)

        # click pe dropdown
        dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()

        # click pe opțiune
        option_locator = (By.XPATH, f"//div[@role='option' and normalize-space()='{option_text}']")
        option = wait.until(EC.element_to_be_clickable(option_locator))
        option.click()


    def verify_current_url(self, expected_url):
        print("EXPECTED:", expected_url)
        print("ACTUAL:", self.driver.current_url)
        assert self.driver.current_url == expected_url, (
            f"Expected URL: {expected_url}, "
            f"but got: {self.driver.current_url}"
        )


    def verify_text(self, locator, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )

        actual_text = self.find(locator).text

        assert actual_text == expected_text, (
            f"Expected text '{expected_text}', "
            f"but got '{actual_text}'"
        )