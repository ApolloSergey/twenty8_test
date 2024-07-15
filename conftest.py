import pytest
from utils.browser import Browser


@pytest.fixture()
def base_driver_setup(request):
    browser = Browser()
    driver = browser.get_browser("Chrome")
    browser.open_webpage(driver, "https://testprojecturl/login")
    request.cls.driver = driver
    yield
    driver.quit()

