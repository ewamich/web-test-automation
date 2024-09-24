from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MyAccountPage(BasePage):
    """
    Page Object Model (POM) for the My Account page.

    This class provides methods for interacting with elements on the My Account page.
    """
    # Locators for elements on the My Account page
    welcome_message = (By.XPATH, "//p[contains(text(), 'Welcome to your account.')]")
    logout_button = (By.XPATH, "//a[@class='logout']")  # Find the correct locator for the logout link or button
    account_created_message = (By.XPATH, "//p[contains(text(), 'Your account has been created.')]")

    def is_welcome_message_displayed(self):
        """
        Check if the welcome message is displayed after successful login.

        :return: True if the welcome message is visible, False otherwise.
        """
        return self.find(self.welcome_message).is_displayed()

    def is_account_created_message_displayed(self):
        """
        Check if the account creation confirmation message is displayed.

        :return: True if the confirmation message is visible, False otherwise.
        """
        return self.find(self.account_created_message).is_displayed()

    def logout(self):
        """
        Click the logout button to log out from the account.
        """
        self.find(self.logout_button).click()  # Click on the logout button to log out
