from playwright.sync_api import expect
from pages.footer_component import  FooterComponent
from pages.home_page import HomePage
import  allure
from utils.tools import take_screenshot


def test_scroll_up_using_arrow_button(page, base_url):
    home_page = HomePage(page)
    footer = FooterComponent(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')
        take_screenshot(page)

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()
        take_screenshot(page)

    with allure.step("Scroll down page to bottom"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        take_screenshot(page)

    with allure.step("Verify 'SUBSCRIPTION' is visible"):
        expect(footer.subscription_label).to_be_visible()
        take_screenshot(page)

    with allure.step("Click on arrow at bottom right side to move upward"):
        home_page.scroll_to_top_button.click()
        take_screenshot(page)

    with allure.step("Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen"):
        expect(home_page.practice_website_label).to_be_visible()
        expect(home_page.practice_website_label).to_have_text("Full-Fledged practice website for Automation Engineers")
        take_screenshot(page)




