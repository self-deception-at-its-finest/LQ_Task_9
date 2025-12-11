from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.header_component import HeaderComponent


class HomePage(BasePage):
    ENDPOINT = ''

    def __init__(self, page: Page):
        super().__init__(page)
        self.header_component = HeaderComponent(page)
        self.slider = page.locator("#slider")
        self.practice_website_label = page.get_by_role("heading", name="Full-Fledged practice website")

    def verify_home_page_visible(self):
        expect(self.page).to_have_title("Automation Exercise")
        expect(self.header_component.header).to_be_visible()
        expect(self.slider).to_be_visible()

    def open(self):
        super().open(self.ENDPOINT)
