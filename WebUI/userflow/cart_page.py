from playwright.sync_api import sync_playwright
from playwright.sync_api import Page


class SwagLabsCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.homepage_locator = "#header_container"
        self.first_item_locator = "#item_4_title_link"
        self.add_to_cart_locator = "button.btn_inventory"
        self.cart_icon_locator = ".shopping_cart_link"
        self.cart_item_locator = ".cart_item"

    def navigate_to_homepage(self):
        self.page.goto("https://www.saucedemo.com/v1/inventory.html")

    def click_first_item(self):
        self.page.click(self.first_item_locator)

    def add_to_cart(self):
        self.page.click(self.add_to_cart_locator)

    def open_cart(self):
        self.page.click(self.cart_icon_locator)

    def is_item_in_cart(self) -> bool:
        return self.page.is_visible(self.cart_item_locator)

