from playwright.sync_api import Page
from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    ENDPOINT = 'account_created'

    def __init__(self, page: Page):
        super().__init__(page)
        self.acc_created_confirmation_msg = page.locator("[data-qa='account-created']")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def open(self):
        super().open(self.ENDPOINT)