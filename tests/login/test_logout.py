from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
import  allure
import os
import pytest

#@pytest.mark.skip(reason="Тест временно отключен")
def test_logout(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)
    login_page = LoginPage(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()

    with allure.step("Verify that 'Signup / Login' button is visible and click it"):
        expect(header.login_button).to_be_visible()
        header.login_button.click()

    with allure.step("Verify 'Login to your account' is visible"):
        expect(login_page.login_title).to_be_visible()

    with allure.step("Enter valid credentials"):
        login_page.login_with_credentials(os.getenv("TEST_USER_EMAIL"), os.getenv("TEST_USER_PASSWORD"))  #??

    with allure.step("Click 'login' button"):
        login_page.login_button.click()

    with allure.step("Verify that home page and 'Logged in as username' is visible"):
        expect(page).to_have_url(base_url + '/')
        expect(page).to_have_title("Automation Exercise")
        expect(header.logged_as_label).to_be_visible()
        expect(header.logged_as_label).to_have_text("Logged in as " + os.getenv("TEST_USER_NAME"))  # ????????????????????????

    with allure.step("Click 'Logout' button"):
        expect(header.logout_button).to_be_visible()
        header.logout_button.click()

    with allure.step("Verify that user is navigated to login page"):
        expect(page).to_have_url(base_url + '/' + login_page.ENDPOINT)

