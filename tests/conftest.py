import pytest
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture(autouse=True)
def accept_cookies(page):
    page.goto("https://www.automationexercise.com/")
    try:
        page.locator('.fc-button.fc-cta-consent.fc-primary-button').click(timeout=3000)
    except:
        pass

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    yield page
    context.close()
