from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
from faker import Faker
import  allure
from utils.tools import take_screenshot


def test_login_with_invalid_credentials(page, base_url):
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

    with allure.step("Verify 'Login to your account' is visible"):
        expect(login_page.login_title).to_be_visible()
        take_screenshot(page)

    with allure.step("Enter incorrect email and password"):
        login_page.login_with_credentials(fake.email(), fake.password())
        take_screenshot(page)

    with allure.step("Click 'login' button"):
        login_page.login_button.click()
        take_screenshot(page)

    with allure.step("Verify error 'Your email or password is incorrect!' is visible"):
        expect(page).to_have_url(base_url + '/' + login_page.ENDPOINT)
        expect(login_page.invalid_login_email_or_password_msg).to_be_visible()
        expect(login_page.invalid_login_email_or_password_msg).to_have_css("color", "rgb(255, 0, 0)")
        take_screenshot(page)
