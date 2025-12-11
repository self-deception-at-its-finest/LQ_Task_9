from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.scroll_to_top_button = page.locator("#scrollUp")

    def open(self, path: str = ''):
        self.page.goto('/' + path)