from playwright.sync_api import Page
from pages.base_page import BasePage
import random


class ProductsPage(BasePage):
    ENDPOINT = '/products'

    def __init__(self, page: Page):
        super().__init__(page)
        self.products_list = page.locator(".single-products")
        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")

    def add_random_product_in_cart(self):
        count = self.products_list.count()
        idx = random.randint(0, count - 1)
        product = self.products_list.nth(idx)
        product.scroll_into_view_if_needed()
        price = int(product.locator("h2").first.inner_text().split()[1])
        name = product.locator("p").first.inner_text()
        product.scroll_into_view_if_needed()
        product.locator(".productinfo .add-to-cart").click()
        self.continue_shopping_btn.wait_for(state="visible", timeout=10000)
        self.continue_shopping_btn.click()
        return {"product_price": price, "product_name": name}

    def open(self):
        super().open(self.ENDPOINT)