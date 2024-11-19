from behave import given, when, then
from WebUI.userflow.cart_page import SwagLabsCartPage


@given("I am on the SwagLabs homepage")
def step_impl(context):
    context.cart_page = SwagLabsCartPage(context.page)
    context.cart_page.navigate_to_homepage()


@when("I click on the first item")
def step_impl(context):
    context.cart_page.click_first_item()


@when("I add it to the cart")
def step_adding_to_cart(context):
    context.cart_page.add_to_cart()


@when("I click on cart icon")
def step_impl(context):
    context.cart_page.open_cart()


@then("I should see the item in the shopping cart")
def step_verify_homepage(context):
    assert context.cart_page.is_item_in_cart(), "The item is not in the shopping cart"


