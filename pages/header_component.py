from playwright.sync_api import Page


class HeaderComponent():
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("#header")
        self.login_button = page.locator("a[href='/login']")
        self.logout_button = page.locator("a[href='/logout']")
        self.products_button = page.locator("a[href='/products']")
        self.cart_button = page.locator(".navbar-nav li a[href='/view_cart']")
        self.test_cases_button = page.locator(".navbar-nav li a[href='/test_cases']")
        self.delete_acc_button = page.locator("a[href='/delete_account']")
        self.contact_us_button = page.locator("a[href='/contact_us']")
        self.logged_as_label = page.get_by_text("Logged in as")