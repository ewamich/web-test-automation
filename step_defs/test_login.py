from pytest_bdd import scenarios, given, when, then
from page_objects.login_page import LoginPage
from page_objects.my_account_page import MyAccountPage

# Load the feature file
scenarios('../features/login.feature')


@given("the user navigates to the login page")
def navigate_to_login_page(go_to_login_page):
    """
    Step definition for navigating to the login page.

    Uses the fixture to open the login page URL.
    """
    pass


@when("the user enters valid credentials")
def enter_valid_credentials(browser, credentials):
    """
    Step definition for entering valid login credentials.

    Retrieves valid credentials from the LoginPage object and performs the login action.
    """
    login_page = LoginPage(browser)
    valid_credentials = credentials['valid']
    login_page.execute_login(valid_credentials['username'], valid_credentials['password'])


@when("the user enters invalid credentials")
def enter_invalid_credentials(browser, credentials):
    """
    Step definition for entering invalid login credentials.

    Retrieves invalid credentials and attempts to log in.
    """
    login_page = LoginPage(browser)
    invalid_credentials = credentials['invalid']
    login_page.execute_login(invalid_credentials['username'], invalid_credentials['password'])


@then("the user should be logged in and see the welcome message")
def my_account_page_is_opened(browser):
    """
    Step definition for verifying successful login.

    Asserts that the user is on the My Account page and the welcome message is displayed.
    """
    expected_page = 'http://www.automationpractice.pl/index.php?controller=my-account'
    current_page = browser.current_url
    assert current_page == expected_page, 'My account page was not opened. Expected url {expected_page}, but got {current_page}'

    my_account_page = MyAccountPage(browser)
    assert my_account_page.is_welcome_message_displayed(), "Welcome message is not displayed"

    my_account_page.logout()


@then("the user should see an error message")
def invalid_credentials_error_is_displayed(browser):
    """
    Step definition for verifying an error message appears when invalid credentials are used.
    """
    login_page = LoginPage(browser)
    assert login_page.is_error_message_displayed(), "Error message is not displayed"
