from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import AccountDeletedPage
import random
from faker import Faker
import  allure
from utils.tools import take_screenshot


def test_registration(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)
    login_page = LoginPage(page)
    fake = Faker()
    signup_page = SignupPage(page)
    acc_created_page = AccountCreatedPage(page)
    acc_deleted_page = AccountDeletedPage(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')
        take_screenshot(page)

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()
        take_screenshot(page)

    with allure.step("Verify that 'Signup / Login' button is visible and click it"):
        expect(header.login_button).to_be_visible()
        header.login_button.click()
        take_screenshot(page)

    with allure.step("Verify 'New User Signup!' is visible"):
        expect(login_page.new_user_signup_title).to_be_visible()
        take_screenshot(page)

    with allure.step("Enter name and email address"):
        fake_name = fake.name()
        fake_email =  fake.word() + fake.email()
        login_page.name_input.fill(fake_name)
        login_page.email_input.fill(fake_email)
        expect(login_page.name_input).to_have_value(fake_name)
        expect(login_page.email_input).to_have_value(fake_email)
        take_screenshot(page)

    with allure.step("Click 'Signup' button"):
        login_page.signup_button.click()
        take_screenshot(page)

    with allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
        expect(signup_page.title).to_be_visible()
        take_screenshot(page)

    with allure.step("Fill details: Title, Name, Email, Password, Date of birth"):
        signup_page.gender_male_radiobutton.click()
        signup_page.name_input.fill(fake_name)
        signup_page.password_input.fill(fake.password())
        signup_page.birth_day_dropdown_menu.select_option(value=str(random.randint(1,31)))
        signup_page.birth_month_dropdown_menu.select_option(value=str(random.randint(1, 12)))
        signup_page.birth_year_dropdown_menu.select_option(value=str(random.randint(1900, 2021)))
        take_screenshot(page)

    with allure.step("Select checkbox 'Sign up for our newsletter!'"):
        signup_page.newsletter_checkbox.check()
        take_screenshot(page)

    with allure.step("Select checkbox 'Receive special offers from our partners!'"):
        signup_page.special_offers_checkbox.check()
        take_screenshot(page)

    with allure.step("Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number"):
        signup_page.first_name_input.fill(fake_name)
        signup_page.last_name_input.fill(fake.last_name())
        signup_page.company_input.fill(fake.company())
        signup_page.address_1_input.fill(fake.address())
        signup_page.address_2_input.fill(fake.address())
        signup_page.country_input.select_option(value="India")
        signup_page.state_input.fill(fake.state())
        signup_page.city_input.fill(fake.city())
        signup_page.zipcode_input.fill(fake.zipcode())
        signup_page.mobile_number_input.fill("2322")
        take_screenshot(page)

    with allure.step("Click 'Create Account button'"):
        signup_page.create_acc_button.click()
        take_screenshot(page)

    with allure.step("Verify that 'ACCOUNT CREATED!' is visible"):
        expect(acc_created_page.acc_created_confirmation_msg).to_be_visible()
        expect(acc_created_page.acc_created_confirmation_msg).to_have_text("Account Created!")
        take_screenshot(page)

    with allure.step("Click 'Continue' button"):
        acc_created_page.continue_button.click()
        take_screenshot(page)

    with allure.step("Verify that 'Logged in as username' is visible"):
        expect(header.logged_as_label).to_be_visible()
        expect(header.logged_as_label).to_contain_text(fake_name)
        take_screenshot(page)

    with allure.step("Click 'Delete Account' button"):
        header.delete_acc_button.click()
        take_screenshot(page)

    with allure.step("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
        expect(acc_deleted_page.acc_deleted_confirmation_msg).to_be_visible()
        expect(acc_deleted_page.acc_deleted_confirmation_msg).to_have_text("Account Deleted!")
        acc_deleted_page.continue_button.click()
        take_screenshot(page)






