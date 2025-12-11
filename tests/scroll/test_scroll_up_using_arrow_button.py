from playwright.sync_api import expect
from pages.footer_component import  FooterComponent
from pages.home_page import HomePage
import  allure


def test_scroll_up_using_arrow_button(page, base_url):
    home_page = HomePage(page)
    footer = FooterComponent(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()

    with allure.step("Scroll down page to bottom"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")


    with allure.step("Verify 'SUBSCRIPTION' is visible"):
        expect(footer.subscription_label).to_be_visible()

    with allure.step("Click on arrow at bottom right side to move upward"):
        home_page.scroll_to_top_button.click()

    with allure.step("Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen"):
        expect(home_page.practice_website_label).to_be_visible()
        expect(home_page.practice_website_label).to_have_text("Full-Fledged practice website for Automation Engineers")



