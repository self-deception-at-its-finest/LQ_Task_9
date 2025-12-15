#  Automation Exercise Testing 

A comprehensive tests automation  for [Automation Exercise](https://www.automationexercise.com) website using Python, Playwright, Pytest, and Allure.

## 📋 Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)


## 🚀 Requirements

### System Requirements
- **Python**: 3.9 or higher
- **Node.js**: 16+ (for Playwright)
- **Git**: For version control

### Python Packages
Core dependencies (see `requirements.txt`):

## 📦 Installation
```bash
git clone https://github.com/self-deception-at-its-finest/LQ_Task_9
cd Task_9

# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Copy example environment file
copy env.example .env
```

## 📁 Project Structure
```bash
Task_9/
│
├── .github/workflows/              # CI/CD Pipelines
│   └── tests.yml                   # GitHub Actions workflow
│
├── pages/                          # Page Object Models
│   ├── base_page.py               # Abstract base page
│   ├── home_page.py               # Home page actions
│   ├── login_page.py              # Login functionality
│   ├── signup_page.py             # User registration
│   ├── products_page.py           # Product catalog
│   ├── cart_page.py               # Shopping cart
│   ├── contact_us_page.py         # Contact form
│   ├── account_created_page.py    # Post-registration
│   ├── delete_account_page.py     # Account deletion
│   ├── header_component.py        # Header navigation
│   └── footer_component.py        # Footer elements
│
├── tests/                          # Test Suites
│   ├── login/                     # Authentication tests
│   │   ├── test_login_with_valid_credentials.py
│   │   ├── test_login_with_invalid_credentials.py
│   │   └── test_logout.py
│   │
│   ├── registration/              # User registration tests
│   │   ├── test_register_user.py
│   │   └── test_registration_with_existing_email.py
│   │
│   ├── cart/                      # Shopping cart tests
│   │   └── test_adding_products_in_cart.py
│   │
│   ├── contact_us_form/           # Contact form tests
│   │   └── test_valid_contact_us_form_submitting.py
│   │
│   ├── footer/                    # Footer tests
│   │   └── test_subscription.py
│   │
│   ├── scroll/                    # UI interaction tests
│   │   └── test_scroll_up_using_arrow_button.py
│   │
│   └── test_cases/                # Test cases page tests
│       └── test_test_cases_page.py
│
├── test_data/                     # Test data files
│
├── utils/                         # Utility functions
│   └── tools.py                 # Common helpers
│
├── conftest.py                    # Pytest fixtures
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
├── .env.example                   # Environment template
├── .gitignore                     # Git ignore rules
└── README.md                      # This documentation
```
## 📁 Running tests
```bash
# Run all tests
pytest

# Run specific test module
pytest tests/login/test_login_with_valid_credentials.py

# Run specific test function
pytest tests/cart/test_adding_products_in_cart.py::test_adding_products_in_cart

# Run with browser UI visible
pytest --headed

# Run in headless mode (default)
pytest --headless

# Run tests in parallel
pytest -n 4

# Run with specific browser
pytest --browser=firefox

# Run only login tests
pytest tests/login/

# Run only cart tests
pytest tests/cart/

# Run by marker
pytest -m smoke
pytest -m regression
```

## 📊 Reporting
When running the `test.yml` workflow, the HTML report is deployed to the `test-reports` branch. The GitHub Pages feature is enabled in this branch, and you can view the deployed report by following this [link](https://self-deception-at-its-finest.github.io/LQ_Task_9/).
```bash
# Generate Allure results
pytest --alluredir=reports/allure-results

# Generate HTML report
allure generate reports/allure-results -o reports/allure-report --clean

# Serve interactive report
allure serve reports/allure-results