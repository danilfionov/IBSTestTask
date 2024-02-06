import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_registration.test_Registration import TestRegistrationApi
from tests.ui.configuration.conftest import driver


class TestRegistration:
    def test_registration_successful_ui(self, driver):
        status_code = 200
        api = TestRegistrationApi.test_successful_registration_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Register - successful")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_registration_unsuccessful_ui(self, driver):
        status_code = 400
        api = TestRegistrationApi.test_unsuccessful_registration_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Register - unsuccessful")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response
