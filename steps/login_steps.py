from behave import given, when, then

@given("Navigate to OrangeHRM page")
def steps_impl(context):
    context.login_page.open()


@when('Enter "{user_text}" in the username input field')
def steps_impl(context, user_text):
    context.login_page.set_username(user_text)


@when('Enter "{pass_text}" in the password input field')
def steps_impl(context, pass_text):
    context.login_page.set_password(pass_text)


@when('Click the Login button')
def steps_impl(context):
    context.login_page.click_button()


@then('The url of the new page is "{expected_url}"')
def steps_impl(context, expected_url):
    context.login_page.verify_current_url(expected_url)


@then('The header text of the new page is "{expected_text}"')
def steps_impl(context, expected_text):
    context.login_page.verify_text(
        context.login_page.DASHBOARD_HEADER,
        expected_text
    )


@then('The error text for the invalid password is "{expected_text}"')
def step_impl(context, expected_text):
    context.login_page.verify_text(
        context.login_page.LOGIN_ERROR_TEXT,
        expected_text
    )


@then("The user remains on the Login page")
def step_impl(context):
    context.login_page.verify_current_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )
