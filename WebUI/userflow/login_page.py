
from playwright.sync_api import Page


class SwagLabsLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.homepage_element = "div#header_container"

    def navigate_to_page(self):
        self.page.goto("https://www.saucedemo.com/v1/")

    def enter_username(self, username: str):
        self.page.fill(self.username_input, username)

    def enter_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def is_homepage_displayed(self):
        return self.page.is_visible(self.homepage_element)
