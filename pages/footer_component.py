from playwright.sync_api import Page


class FooterComponent():
    def __init__(self, page: Page):
        self.page = page
        self.subscription_label = page.get_by_role("heading", name="Subscription")
        self.subscription_email_input = page.locator("input[id='susbscribe_email']")
        self.subscription_button = page.locator("button[id='subscribe']")
        self.successful_subscription_msg = page.locator("#success-subscribe")