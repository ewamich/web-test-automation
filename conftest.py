import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    """
    Fixture to initialize and return a WebDriver instance for each test.

    This fixture creates a new browser instance for each test, waits for elements implicitly, and closes the browser after each test.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def go_to_login_page(browser):
    """
    Fixture to navigate to the login page of the automation practice website.

    This fixture opens the login page URL in the browser and waits for the email input field
    to be visible to ensure that the page has fully loaded before running the tests.

    :param browser: The Selenium WebDriver instance provided by the browser fixture.
    """
    browser.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    # Ensure the page is fully loaded
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )

@pytest.fixture(scope="session")
def credentials():
    """
    Fixture to load user credentials from a JSON file.

    This fixture reads the credentials from the 'credentials.json' file
    and returns them as a dictionary. The scope is set to 'session'
    so that the credentials are loaded once per test session,
    which improves efficiency by avoiding repeated file I/O.

    :return: A dictionary containing user credentials.
    """
    with open('credentials.json') as f:
        return json.load(f)
