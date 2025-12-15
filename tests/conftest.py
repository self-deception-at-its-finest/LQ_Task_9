import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(autouse=True)
def accept_cookies(page, base_url):
    page.goto(base_url)
    try:
        page.locator('.fc-button.fc-cta-consent.fc-primary-button').click(timeout=3000)
    except:
        pass

@pytest.fixture(scope="session")
def base_url():
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise RuntimeError("BASE_URL is not set in .env or environment variables")
    return base_url

@pytest.fixture(autouse=True)
def configure_page(page):
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    return page