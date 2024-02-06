import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_login.test_Login import TestLoginApi
from tests.ui.configuration.conftest import driver


class TestLogin:
    def test_login_successful_ui(self, driver):
        status_code = 200
        api = TestLoginApi.test_successful_login_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Login - successful")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_login_unsuccessful_ui(self, driver):
        status_code = 400
        api = TestLoginApi.test_unsuccessful_login_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Login - unsuccessful")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response
