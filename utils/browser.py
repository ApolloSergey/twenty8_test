import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class Browser(object):
    def set_browser(self, browser):
        driver = None
        logging.info("Browser: " + browser)
        if browser in "Chrome":
            chrome_options = Options()
            chrome_options.add_argument("--kiosk")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                      options=chrome_options)
        return driver

    def get_browser(self, browser):
        return self.set_browser(browser)

    def open_webpage(self, driver, url):
        logging.info("Open web page: %s", str(url))
        driver.get(url)
        logging.debug("Web page has been opened")


browser_element = Browser()