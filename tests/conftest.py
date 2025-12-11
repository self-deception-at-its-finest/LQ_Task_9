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
    """Фикстура для получения base_url"""
    return request.config.getoption("--base-url")