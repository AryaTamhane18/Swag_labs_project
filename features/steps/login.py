from behave import given, when, then
from WebUI.userflow.login_page import SwagLabsLoginPage


@given("user navigates to the SwagLab page")
def step_navigate_to_swagLabs(context):
    context.page_class = SwagLabsLoginPage(context.page)
    context.page_class.navigate_to_page()


@when('user enters the "{username}"')
def step_enter_username(context, username):
    context.page_class.enter_username(username)


@when('user enters "{password}"')
def step_enter_password(context, password):
    context.page_class.enter_password(password)


@when("user clicks on the login button")
def step_click_login(context):
    context.page_class.click_login()


@then("user should see the homepage if credentials are valid")
def step_verify_login(context):
    assert context.page_class.is_homepage_displayed(), "Homepage is not displayed"


# @then("user should see an error message if credentials are invalid")
# def step_error_message(context):
#     assert context.page_class.is_error_displayed(), "error message is not displayed for invalid credentials"

