from playwright.sync_api import expect
from pages.footer_component import FooterComponent
from pages.home_page import HomePage
from faker import Faker
import allure


def test_subscription(page, base_url):
    home_page = HomePage(page)
    fake = Faker()
    footer = FooterComponent(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()

    with allure.step("Scroll down to footer"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    with allure.step("Verify text 'SUBSCRIPTION'"):
        expect(footer.subscription_label).to_be_visible()

    with allure.step("Enter email address in input and click arrow button"):
        footer.subscription_email_input.fill(fake.email())
        footer.subscription_button.click()

    with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
        expect(footer.successful_subscription_msg).to_be_visible()
        expect(footer.successful_subscription_msg).to_have_text("You have been successfully subscribed!")