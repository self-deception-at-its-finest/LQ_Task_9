import os
from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
from faker import Faker
import  allure
from utils.tools import take_screenshot


def test_registration(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)
    login_page = LoginPage(page)
    fake = Faker()

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
        login_page.name_input.fill(fake_name)
        login_page.email_input.fill(os.getenv("TEST_USER_EMAIL"))
        expect(login_page.name_input).to_have_value(fake_name)
        expect(login_page.email_input).to_have_value(os.getenv("TEST_USER_EMAIL"))
        take_screenshot(page)

    with allure.step("Click 'Signup' button"):
        login_page.signup_button.click()
        take_screenshot(page)

    with allure.step(" Verify error 'Email Address already exist!' is visible"):
        expect(page).to_have_url("https://www.automationexercise.com/signup")
        expect(login_page.invalid_signup_existing_email_msg).to_be_visible()
        expect(login_page.invalid_signup_existing_email_msg).to_have_css("color", "rgb(255, 0, 0)")
        take_screenshot(page)




