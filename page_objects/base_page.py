from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class for all Page Objects.

    This class provides common methods and utilities that can be inherited by specific page objects,
    such as element finding, waiting, and action chaining.
    """

    def __init__(self, browser):
        """
        Constructor to initialize the browser, WebDriverWait, and ActionChains.

        :param browser: The Selenium WebDriver instance.
        """
        self.browser = browser
        self._wait = WebDriverWait(self.browser, 10)
        self._action = ActionChains(self.browser)

    def find(self, locator):
        """
        Find a single element on the page.

        :param locator: Locator tuple (By, value) to find the element.
        :return: The WebElement found by the locator.
        """
        return self.browser.find_element(*locator)

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for specific element is located on the page.

        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
