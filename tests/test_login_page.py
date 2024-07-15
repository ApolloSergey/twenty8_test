import pytest
from pages.login_page import LoginPage
from utils.helpers.verify import Verify


class TestLoginPage:
    """
    Perform tests for Login page
    """

    @pytest.mark.usefixtures("base_driver_setup")
    def test_open_login_page(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        Verify.true(login_page.are_login_page_controls_displayed(), "Controls are missing on Login page")

    @pytest.mark.usefixtures("base_driver_setup")
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        login_page.perform_login("xxx", "yyy")
        Verify.equals(login_page.is_success_message_during_login_displayed(), "success",
                      "Success message is missing")
        Verify.false(login_page.is_login_page_displayed(), "Login page is displayed")

    @pytest.mark.usefixtures("base_driver_setup")
    def test_invalid_email_login(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        login_page.perform_login("zzz", "yyy")
        Verify.equals(login_page.is_error_message_during_login_displayed(), "invalid email",
                      "Error message is missing")
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")

    @pytest.mark.usefixtures("base_driver_setup")
    def test_invalid_email_and_password_login(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        login_page.perform_login("zzz", "iii")
        Verify.equals(login_page.is_error_message_during_login_displayed(), "enter valid email",
                      "Error message is missing")
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")

    @pytest.mark.usefixtures("base_driver_setup")
    def test_empty_email_login(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        login_page.perform_login("", "yyy")
        Verify.equals(login_page.is_empty_error_message_during_login_displayed(), "empty field value error",
                      "Empty error message is missing")
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")

    @pytest.mark.usefixtures("base_driver_setup")
    def test_empty_password_login(self):
        login_page = LoginPage(self.driver)
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
        login_page.perform_login("xxx", "")
        Verify.equals(login_page.is_empty_error_message_during_login_displayed(), "empty field value error",
                      "Empty error message is missing")
        Verify.true(login_page.is_login_page_displayed(), "Login page is missing")
