import pytest
from pages.questions_page import QuestionsPage
from utils.helpers.verify import Verify


class TestQuestionPage:
    """
    Perform tests for Question page
    """

    @pytest.mark.usefixtures("base_driver_setup")
    def test_select_radio_button_for_each_question(self):
        question_page = QuestionsPage(self.driver)
        Verify.true(question_page.select_random_value_in_radio_button_question(),
                    "Some question have unselected radio buttons")
