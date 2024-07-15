import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper


class LoginPage(BasePage):
    """
    Locators and actions of the Login Page
    """

    USER_NAME = (By.ID, "username")
    USER_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "kc-login")
    ERROR_MESSAGE = (By.ID, "error_message_placeholder")
    SUCCESS_MESSAGE = (By.ID, "success_message_placeholder")
    EMPTY_MESSAGE = (By.ID, "empty_message_placeholder")

    def is_login_page_displayed(self):
        logging.info("Verify that the login page is displayed")
        result = [UiHelper.wait_till_element_is_displayed(self.driver, self.USER_NAME),
                  "Log In" in self.driver.title]
        return all(result)

    def are_login_page_controls_displayed(self):
        logging.info("Verify that the login page controls are displayed")
        result = [UiHelper.wait_till_element_is_displayed(self.driver, self.USER_NAME),
                  UiHelper.wait_till_element_is_displayed(self.driver, self.USER_PASSWORD),
                  UiHelper.wait_till_element_is_displayed(self.driver, self.LOGIN_BUTTON)]
        return all(result)

    def is_success_message_during_login_displayed(self):
        logging.info("Verify that the success message is displayed")
        success_message = self.driver.find_element(*self.SUCCESS_MESSAGE).text
        assert success_message

    def is_error_message_during_login_displayed(self):
        logging.info("Verify that the error message is displayed")
        error_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        assert error_message

    def is_empty_error_message_during_login_displayed(self):
        logging.info("Verify that the empty error message is displayed")
        error_message = self.driver.find_element(*self.EMPTY_MESSAGE).text
        assert error_message

    def perform_login(self, user_name, user_password):
        logging.info("Perform login with user credentials")
        UiHelper.wait_till_element_is_displayed(self.driver, self.USER_NAME)
        self.driver.find_element(*self.USER_NAME).send_keys(user_name)
        UiHelper.wait_till_element_is_displayed(self.driver, self.USER_PASSWORD)
        self.driver.find_element(*self.USER_PASSWORD).send_keys(user_password)
        UiHelper.wait_till_element_clickable(self.driver, self.LOGIN_BUTTON)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
