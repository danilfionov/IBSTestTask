import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_miscellaneous.test_Delayed_Response import TestDelayedResponseApi
from tests.ui.configuration.conftest import driver


class TestDelayedResponse:
    def test_delayed_response_ui(self, driver):
        status_code = 200
        api = TestDelayedResponseApi.test_delayed_response_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Delayed response")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response
