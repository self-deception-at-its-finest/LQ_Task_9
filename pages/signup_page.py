from playwright.sync_api import Page
from pages.base_page import BasePage


class SignupPage(BasePage):
    ENDPOINT = 'signup'

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_acc_button = page.locator("[data-qa='create-account']")

        #Account Information Form locators
        self.title = page.get_by_role("heading", name="Enter Account Information")
        self.gender_male_radiobutton = page.locator("#id_gender1")
        self.gender_female_radiobutton = page.locator("#id_gender2")
        self.name_input = page.locator("[data-qa='name']")
        self.email_input = page.locator("[data-qa='email']")
        self.password_input = page.locator("[data-qa='password']")
        self.birth_day_dropdown_menu = page.locator("[data-qa='days']")
        self.birth_month_dropdown_menu = page.locator("[data-qa='months']")
        self.birth_year_dropdown_menu = page.locator("[data-qa='years']")
        self.newsletter_checkbox = page.locator("input[id='newsletter']")
        self.special_offers_checkbox = page.locator("input[id='optin']")

        #Address Information Form locators
        self.first_name_input = page.locator("[data-qa='first_name']")
        self.last_name_input = page.locator("[data-qa='last_name']")
        self.company_input = page.locator("[data-qa='company']")
        self.address_1_input = page.locator("[data-qa='address']")
        self.address_2_input = page.locator("[data-qa='address2']")
        self.country_input = page.locator("[data-qa='country']")
        self.state_input = page.locator("[data-qa='state']")
        self.city_input = page.locator("[data-qa='city']")
        self.zipcode_input = page.locator("[data-qa='zipcode']")
        self.mobile_number_input = page.locator("[data-qa='mobile_number']")

    def open(self):
        super().open(self.ENDPOINT)