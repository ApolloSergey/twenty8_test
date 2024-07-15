import logging
import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper


class QuestionsPage(BasePage):
    """
    Locators and actions of the Questions Page
    """
    RADIO_BUTTON_QUESTION = (By.CLASS_NAME, "selectmanycheckbox-field")
    QUESTION_RADIO_BUTTONS = (By.XPATH, ".//input[@type='radio']")

    def select_random_value_in_radio_button_question(self):
        logging.info("Select random radio button value for each question")
        UiHelper.wait_till_element_is_displayed(self.driver, self.RADIO_BUTTON_QUESTION)
        tables = self.driver.find_elements(*self.RADIO_BUTTON_QUESTION)
        result = []
        for table in tables:
            radio_buttons = table.find_elements(*self.QUESTION_RADIO_BUTTONS)
            chosen_radio = random.choice(radio_buttons)
            chosen_radio.click()
            result.append(chosen_radio.is_selected())
        return result
