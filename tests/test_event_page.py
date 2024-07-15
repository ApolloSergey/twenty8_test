import pytest
from pages.events_page import EventsPage
from utils.helpers.verify import Verify


class TestEventsPage:
    """
    Perform tests for Events page
    """

    @pytest.mark.usefixtures("base_driver_setup")
    def test_select_event_in_dropdown_menu(self):
        event_page = EventsPage(self.driver)
        event_page.select_item_in_event_dropdown_menu("D2 approval by Advisory Committee")
        Verify.equals(event_page.get_event_dropdown_value(), "D2 approval by Advisory Committee",
                      "Value not selected")
