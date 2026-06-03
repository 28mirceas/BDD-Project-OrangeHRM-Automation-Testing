from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DashboardPage(BasePage):

    BUTTON_PIM = (By.XPATH, "//a[contains(@href,'pim')]")


    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_dashboard_ready(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )


    def click_pim(self):
        pim = self.wait.until(
            EC.presence_of_element_located(self.BUTTON_PIM)
        )
        self.driver.execute_script("arguments[0].click();", pim)


