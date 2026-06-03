from behave import given, when, then

@when('Click the Add Employee button')
def steps_impl(context):
    context.employee_page.click_add_employee()

@when('Enter "{first_name_text}" in the First Name input field')
def steps_impl(context, first_name_text):
    context.employee_page.set_first_name(first_name_text)

@when('Enter "{last_name_text}" in the Last Name input field')
def steps_impl(context, last_name_text):
    context.employee_page.set_last_name(last_name_text)

@when('Enter employee id in the Employee Id input field')
def steps_impl(context):
    context.employee_page.set_employee_id()

@when('Click Save button')
def steps_impl(context):
    context.employee_page.click_save()

@then('The employee name in Personal Details page which is created is "{personal_page_name}"')
def steps_impl(context, personal_page_name):#
    context.employee_page.verify_text(context.employee_page.PERSONAL_PAGE_NAME,personal_page_name)


@then('The error text for missing mandatory fields is "{error_text}"')
def steps_impl(context, error_text):
    context.employee_page.verify_text(context.employee_page.ERROR_MESSAGE,error_text)


@when('Click button Employee List')
def steps_impl(context):
    context.employee_page.click_employee_list()



@when('Click on the user dropdown menu')
def steps_impl(context):
    context.employee_page.click_user_dropdown_menu()


@when('Click Logout button')
def steps_impl(context):
    context.employee_page.click_logout_button()


@then('The user is redirected to page "{expected_url}"')
def steps_impl(context, expected_url):
    context.employee_page.verify_current_url(expected_url)


@then('Login page is displayed')
def steps_impl(context):
    context.employee_page.verify_login_page_displayed()