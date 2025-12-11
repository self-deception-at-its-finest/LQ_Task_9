from playwright.sync_api import Page
from pages.base_page import BasePage


class AccountDeletedPage(BasePage):
    ENDPOINT = 'delete_account'

    def __init__(self, page: Page):
        super().__init__(page)
        self.acc_deleted_confirmation_msg = page.locator("[data-qa='account-deleted']")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def open(self):
        super().open(self.ENDPOINT)