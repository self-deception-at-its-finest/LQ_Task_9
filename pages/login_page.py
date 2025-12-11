from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    ENDPOINT = 'login'

    def __init__(self, page: Page):
        super().__init__(page)
        self.new_user_signup_title = page.get_by_role("heading", name="New User Signup!")
        self.name_input = page.locator("[data-qa='signup-name']")
        self.email_input = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")
        self.login_title = page.get_by_role("heading", name="Login to your account")
        self.login_email_input = page.locator("[data-qa='login-email']")
        self.login_password_input = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")
        self.invalid_login_email_or_password_msg = page.get_by_text("Your email or password is incorrect!")
        self.invalid_signup_existing_email_msg = page.get_by_text("Email Address already exist!")

    def login_with_credentials(self, email="", password=""):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)

    def open(self):
        super().open(self.ENDPOINT)