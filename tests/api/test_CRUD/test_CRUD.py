from python.api.register.api import CRUD
from python.api.register.models import CRUD_User
from schemas.resources import valid_schema_list, invalid_schema
from tests.api.configuration.conftest import url


class TestCRUDApi:
    def test_post_create(self, url):
        body = CRUD_User.get_user_create()
        response = CRUD(url).create(body=body, schema=valid_schema_list)
        assert response.status == 201
        assert response.response.get('name') == "morpheus"
        assert response.response.get('job') == "leader"
        return response

    def test_put_update(self, url):
        body = CRUD_User.get_user_update()
        response = CRUD(url).put_update(body=body, schema=invalid_schema)
        assert response.status == 200
        assert response.response.get('name') == "morpheus"
        assert response.response.get('job') == "zion resident"
        return response

    def test_patch_update(self, url):
        body = CRUD_User.get_user_update()
        response = CRUD(url).patch_update(body=body, schema=invalid_schema)
        assert response.status == 200
        assert response.response.get('name') == "morpheus"
        assert response.response.get('job') == "zion resident"
        return response

    def test_delete(self, url):
        response = CRUD(url).delete(schema=invalid_schema)
        assert response == 204
        return response
