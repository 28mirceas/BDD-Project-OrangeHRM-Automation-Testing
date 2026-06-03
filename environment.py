from browser import Browser
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeeListPage


def before_scenario(context, scenario):
    context.browser = Browser()

    context.login_page = LoginPage(context.browser.driver)
    context.dashboard_page = DashboardPage(context.browser.driver)
    context.employee_page = EmployeeListPage(context.browser.driver)

    # Login automat doar pentru scenariile cu tag @dashboard
    if "dashboard" in scenario.tags:
        context.login_page.open()
        context.login_page.login("Admin", "admin123")

    # Click PIM automat doar pentru scenariile cu tag @employeelist
    if "employeelist" in scenario.tags:
        context.login_page.open()
        context.login_page.login("Admin", "admin123")
        context.dashboard_page.wait_for_dashboard_ready()
        context.dashboard_page.click_pim()


def after_scenario(context, scenario):
    if hasattr(context, "browser") and context.browser:
        context.browser.close()
        context.browser = None