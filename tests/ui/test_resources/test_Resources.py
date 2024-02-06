import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_resources.test_Resources import TestResourcesApi
from tests.ui.configuration.conftest import driver


class TestResources:
    def test_get_list_resources_ui(self, driver):
        status_code = 200
        api = TestResourcesApi.test_get_list_resources_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("List <resource>")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_get_single_resources_ui(self, driver):
        status_code = 200
        api = TestResourcesApi.test_get_single_resources_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Single <resource>")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response

    def test_single_resources_not_found_ui(self, driver):
        status_code = 404
        api = TestResourcesApi.test_single_resources_not_found_api(self)

        base_page = Main_Page(driver)
        base_page.click_link("Single <resource> not found")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        assert api.response == json_response
