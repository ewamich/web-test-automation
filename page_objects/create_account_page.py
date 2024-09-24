from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class CreateAccount(BasePage):
    """
    Page object model for the account creation page.

    This class encapsulates the elements and actions that can be performed on the
    account creation page of the automation practice website. It inherits from
    the BasePage to leverage common page functionalities.
    """
    # Locators for the account creation form elements
    first_name_input = (By.ID, 'customer_firstname')
    last_name_input = (By.ID, 'customer_lastname')
    password_input = (By.ID, 'passwd')
    register_button = (By.ID, 'submitAccount')
    login_error_message = (By.XPATH, "//p[contains(text(), 'There is 1 error')]")


    def create_new_account(self, first_name: str, last_name: str,  password: str):
        """
        Method to create a new user account.

        This method fills in the first name, last name, and password fields,
        and submits the registration form by clicking the register button.

        :param first_name: The first name of the user.
        :param last_name: The last name of the user.
        :param password: The desired password for the account.
        """
        self.find(self.first_name_input).send_keys(first_name)
        self.find(self.last_name_input).send_keys(last_name)
        self.find(self.password_input).send_keys(password)
        self.find(self.register_button).click()








