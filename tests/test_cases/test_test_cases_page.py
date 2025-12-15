from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
import allure
from utils.tools import take_screenshot


def test_valid_redirect_to_test_cases_page(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')
        take_screenshot(page)

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()
        take_screenshot(page)

    with allure.step("Click on 'Test Cases' button"):
        header.test_cases_button.click()
        take_screenshot(page)

    with allure.step("Verify user is navigated to test cases page successfully"):
        expect(page).to_have_url(base_url + '/test_cases')
        take_screenshot(page)






