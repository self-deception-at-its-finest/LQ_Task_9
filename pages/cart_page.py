from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    ENDPOINT = '/view_cart'

    def __init__(self, page: Page):
        super().__init__(page)
        self.items_description_in_cart_list = page.locator(".cart_description h4 a")
        self.items_price_in_cart_list = page.locator(".cart_price p")

    def open(self):
        super().open(self.ENDPOINT)