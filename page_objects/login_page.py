import json

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object Model (POM) for the Login Page.

    This class provides methods for interacting with the login page, such as
    entering login credentials, submitting the form, and verifying login errors.
    """
    create_email_input = (By.ID, 'email_create')
    username_input = (By.NAME, 'email')
    password_input = (By.ID, 'passwd')
    login_button = (By.ID, 'SubmitLogin')
    create_account_button = (By.ID, 'SubmitCreate')
    invalid_credentials_login_message = (By.XPATH, "//p[contains(text(), 'There is 1 error')]")
    duplicated_email_message = (
    By.XPATH, "//li[contains(text(), 'An account using this email address has already been registered.')]")


    def execute_login(self, username: str, password: str):
        """
        Perform login action by entering the username and password, and clicking the login button.

       :param username: The email/username to log in with.
        :param password: The password to log in with.
       """
        # Enter username and password
        self.find(self.username_input).send_keys(username)
        self.find(self.password_input).send_keys(password)
        self.find(self.login_button).click()

    def register_new_email(self, create_email: str):
        """
        Register a new account by entering an email in the 'create account' input and submitting it.

       :param create_email: The email to register a new account with.
        """
        # Enter the email in the 'create account' input
        self.find(self.create_email_input).send_keys(create_email)
        self.find(self.create_account_button).click()

    def is_error_message_displayed(self):
        """
        Check if the login error message (for invalid credentials) is displayed.

        :return: True if the error message is displayed, False otherwise.
        """
        return self.find(self.invalid_credentials_login_message).is_displayed()

    def is_duplicated_email_error_message_displayed(self):
        """
        Check if the error message for a duplicated registration email is displayed.

        :return: True if the duplicated email error message is displayed, False otherwise.
        """
        return self.find(self.duplicated_email_message).is_displayed()
