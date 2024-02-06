import json

from python.ui.pages.Main_Page import Main_Page
from tests.api.test_CRUD.test_CRUD import TestCRUDApi
from tests.ui.configuration.conftest import driver


class TestCRUD:
    def test_get_create_ui(self, driver):
        status_code = 201
        api = TestCRUDApi.test_post_create(self)

        base_page = Main_Page(driver)
        base_page.click_link("Create")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        # assert api.response == json_response

    def test_put_update_ui(self, driver):
        status_code = 200
        api = TestCRUDApi.test_put_update(self)

        base_page = Main_Page(driver)
        base_page.click_button_type_link_by_number("Update", 1)
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        #assert api.response == json_response

    def test_patch_update_ui(self, driver):
        status_code = 200
        api = TestCRUDApi.test_patch_update(self)

        base_page = Main_Page(driver)
        base_page.click_button_type_link_by_number("Update", 2)
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        json_response = json.loads(response)
        assert api.status == status_code
        # assert api.response == json_response

    def test_delete_ui(self, driver):
        status_code = 204
        api = TestCRUDApi.test_delete(self)

        base_page = Main_Page(driver)
        base_page.click_link("Delete")
        base_page.check_field_is_filled_value("Response", str(status_code))
        response = base_page.get_field_value("Response")
        # json_response = json.loads(response)
        assert api == status_code
        # assert api.response == json_response
