# from playwright.sync_api import expect
# from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
#
#
# class ElementNotInteractableError(Exception):
#     pass
#
# class BaseUIElement:
#     def __init__(self, page: Page, selector: str, timeout: int = 10000):
#         self.page = page
#         self.selector = selector
#         self.timeout = timeout
#
#     def find_element(self):
#         """Locate the element using the selector."""
#         return self.page.locator(self.selector)
#
#     def is_visible(self) -> bool:
#         """Check if the element is visible on the page."""
#         try:
#             return self.page.is_visible(self.selector, timeout=self.timeout)
#         except PlaywrightTimeoutError:
#             return False
#
#     def is_enabled(self) -> bool:
#         """Check if the element is enabled."""
#         element = self.find_element()
#         return element.is_enabled() if element else False
#
#     def click(self):
#         """Click the element if it's interactable."""
#         try:
#             if not self.is_visible() or not self.is_enabled():
#                 raise ElementNotInteractableError(
#                     f"Element with selector '{self.selector}' is not interactable."
#                 )
#             self.find_element().click()
#         except PlaywrightTimeoutError as e:
#             raise PlaywrightTimeoutError(
#                 f"Timed out trying to click element with selector '{self.selector}': {e}"
#             )
