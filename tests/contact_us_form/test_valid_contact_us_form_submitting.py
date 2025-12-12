from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
import random
from faker import Faker
import allure
import pytest

@pytest.mark.one
def test_valid_contact_us_form_submitting(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)
    fake = Faker()
    contact_us_page = ContactUsPage(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + '/')

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()

    with allure.step("Verify that 'Contact Us' button is visible and click it"):
        expect(header.contact_us_button).to_be_visible()
        header.contact_us_button.click()

    with allure.step("Verify 'GET IN TOUCH' is visible"):
        expect(contact_us_page.get_in_touch_label).to_be_visible()

    with allure.step("Enter name, email, subject and message"):
        contact_us_page.name_input.fill(fake.name())
        contact_us_page.email_input.fill(fake.email())
        contact_us_page.subject_input.fill(fake.sentence())
        contact_us_page.message_input.fill(fake.text(random.randint(100, 300)))

    with allure.step("Upload file"):
        test_data_files = ["test_data/meme.jpg",
                           "test_data/test_data_pdf_file.pdf",
                           "test_data/test_data_docx_file.docx"]
        contact_us_page.upload_file_input.set_input_files(random.choice(test_data_files))

    with allure.step("Click 'Submit' button"):
        page.once("dialog", lambda dialog: dialog.accept())
        contact_us_page.submit_button.click(force=True)

    with allure.step("Verify success message 'Success! Your details have been submitted successfully.' is visible"):
        contact_us_page.successful_submit_alert_msg.wait_for(state="visible", timeout=10000)
        expect(contact_us_page.successful_submit_alert_msg).to_be_visible()
        expect(contact_us_page.successful_submit_alert_msg).to_have_text("Success! Your details have been submitted successfully.")

    with allure.step("Click 'Home' button and verify that landed to home page successfully"):
        contact_us_page.home_button.click()
        expect(page).to_have_url(base_url + '/')


