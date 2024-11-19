# # WebUI/button.py
# from WebUI.UIElements.Base_ui_element import BaseUIElement, ElementNotInteractableError
# from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
#
# class Button(BaseUIElement):
#     def __init__(self, page, selector, timeout=10000):
#         super().__init__(page, selector, timeout)
#
#     def click(self):
#         """Override the click method for button-specific behavior if necessary."""
#         super().click()  # Calls the click method from BaseUIElement
