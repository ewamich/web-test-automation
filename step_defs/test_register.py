from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.create_account_page import CreateAccount
from page_objects.login_page import LoginPage
from page_objects.my_account_page import MyAccountPage

# Load the feature file
scenarios('../features/register.feature')


@given("the user navigates to the registration page")
def navigate_to_login_page(browser):
    """
    Step definition for navigating to the registration page.

    This function opens the registration page and waits for the
    email input field to be visible, indicating that the page has loaded.

    :param browser: The Selenium WebDriver instance.
    """
    browser.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    # Ensure the page is fully loaded
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'email_create'))
    )


@when("the user enters valid registration details")
def enter_valid_unregistered_email(browser, credentials):
    """
    Step definition for entering valid registration details.

    This function retrieves unregistered user credentials from the
    provided credentials and submits the registration form.

    :param browser: The Selenium WebDriver instance.
    :param credentials: The dictionary containing user credential data.
    """
    login_page = LoginPage(browser)
    create_account_page = CreateAccount(browser)
    unregistered_credentials = credentials['unregistered']
    login_page.register_new_email(unregistered_credentials['username'])
    create_account_page.create_new_account(unregistered_credentials['first_name'],
                                           unregistered_credentials['last_name'],
                                           unregistered_credentials['password'])


@when("the user enters an email that’s already registered")
def enter_registered_email(browser, credentials):
    """
    Step definition for entering an already registered email.

    This function attempts to register an account with an email that
    is already in use, triggering the duplicate email error.

    :param browser: The Selenium WebDriver instance.
    :param credentials: The dictionary containing user credential data.
    """
    login_page = LoginPage(browser)
    unregistered_credentials = credentials['unregistered']
    login_page.register_new_email(unregistered_credentials['username'])


@then("the user should see a confirmation message")
def confirmation_message_is_displayed(browser):
    """
    Step definition to verify the presence of a confirmation message.

    This function asserts that the welcome message is displayed on
    the My Account page after successful registration.

    :param browser: The Selenium WebDriver instance.
    """
    my_account_page = MyAccountPage(browser)
    assert my_account_page.is_welcome_message_displayed(), "Welcome message is not displayed"


@then("the user should see an error message about duplicated email")
def invalid_credentials_error_is_displayed(browser):
    """
    Step definition to verify the presence of an error message for duplicate email.

    This function asserts that the appropriate error message is displayed
    when attempting to register with an already used email.

    :param browser: The Selenium WebDriver instance.
    """
    login_page = LoginPage(browser)
    assert login_page.is_duplicated_email_error_message_displayed(), "Error message is not displayed"
