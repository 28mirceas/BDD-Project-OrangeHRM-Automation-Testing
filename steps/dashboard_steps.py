from behave import given, when, then

@given('Click on the PIM button on the left menu')
def steps_impl(context):
    context.dashboard_page.wait_for_dashboard_ready()
    context.dashboard_page.click_pim()

@when('The url of the new page is "{expected_url}"')
def steps_impl(context, expected_url):
    context.dashboard_page.verify_current_url(expected_url)