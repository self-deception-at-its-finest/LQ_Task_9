from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    ENDPOINT = 'contact_us'

    def __init__(self, page: Page):
        super().__init__(page)
        self.get_in_touch_label = page.get_by_text("Get In Touch")
        self.name_input = page.locator("[data-qa='name']")
        self.email_input = page.locator("[data-qa='email']")
        self.subject_input = page.locator("[data-qa='subject']")
        self.message_input = page.locator("[data-qa='message']")
        self.upload_file_input = page.locator("input[type='file'][name='upload_file']")
        self.submit_button = page.locator("[data-qa='submit-button']")
        self.successful_submit_alert_msg = page.locator(".status.alert.alert-success")
        self.home_button = page.locator(".btn.btn-success")

    def open(self):
        super().open(self.ENDPOINT)