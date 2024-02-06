from python.api.register.api import Users
from schemas.users import valid_schema_list, invalid_schema
from tests.api.configuration.conftest import url


class TestUsersApi:
    def test_get_list_users_api(self, url):
        response = Users(url).get_list_users(schema=valid_schema_list)
        assert response.status == 200
        assert response.response.get('page') == 2
        assert response.response.get('per_page') == 6
        assert response.response.get('total') == 12
        assert response.response.get('total_pages') == 2
        return response

    def test_get_single_user_api(self, url):
        response = Users(url).get_single_users(schema=invalid_schema)
        assert response.status == 200
        assert response.response.get('data').get('id') == 2
        assert response.response.get('data').get('email') == 'janet.weaver@reqres.in'
        assert response.response.get('data').get('first_name') == 'Janet'
        assert response.response.get('data').get('last_name') == 'Weaver'
        assert response.response.get('data').get('avatar') == 'https://reqres.in/img/faces/2-image.jpg'
        assert response.response.get('support').get('text') == 'To keep ReqRes free, contributions towards server costs are appreciated!'
        assert response.response.get('support').get('url') == 'https://reqres.in/#support-heading'
        return response

    def test_single_user_not_found_api(self, url):
        response = Users(url).get_single_users_not_found(schema=invalid_schema)
        assert response.status == 404
        return response
