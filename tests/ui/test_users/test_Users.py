import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_users.test_Users import TestUsersApi
from tests.ui.configuration.conftest import driver


class TestUsers:
    def test_get_list_users_ui(self, driver):
        status_code = 200
        api = TestUsersApi.test_get_list_users_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("List users")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_get_single_user_ui(self, driver):
        status_code = 200
        api = TestUsersApi.test_get_single_user_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Single user")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_single_user_not_found_ui(self, driver):
        status_code = 404
        api = TestUsersApi.test_single_user_not_found_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Single user not found")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response
