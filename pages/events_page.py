from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper
from selenium.webdriver.support.select import Select


class EventsPage(BasePage):
    """
    Locators and actions of the Events Page
    """
    EVENTS_DROPDOWN_MENU = (By.XPATH, ".//span[@role='listbox']")
    EVENT_IN_MENU = "//li[contains(@class,'ui-autocomplete-list-item') and contains(text(),'{}')]"

    def select_item_in_event_dropdown_menu(self, event_name):
        """
        Select event in dropdown menu , if not visible scroll to it
        """
        event_xpath = self.EVENT_IN_MENU.format(event_name)
        event_element = self.driver.find_element(By.XPATH, event_xpath)
        if UiHelper.wait_till_element_clickable(self.driver, (By.XPATH, event_xpath)):
            event_element.click()
        else:
            UiHelper.scroll_to_element(self.driver, event_element)
            event_element.click()

    def get_event_dropdown_value(self):
        """
        Get value from event dropdown menu
        """
        event_element = self.driver.find_element(*self.EVENTS_DROPDOWN_MENU)
        entity_selector = Select(event_element)
        selected_option = entity_selector.first_selected_option
        return selected_option.text
