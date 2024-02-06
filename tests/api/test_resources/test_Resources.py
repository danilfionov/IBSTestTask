from python.api.register.api import Resources
from schemas.resources import valid_schema_list, invalid_schema
from tests.api.configuration.conftest import url


class TestResourcesApi:
    def test_get_list_resources_api(self, url):
        response = Resources(url).get_list_resources(schema=valid_schema_list)
        assert response.status == 200
        assert response.response.get('page') == 1
        assert response.response.get('per_page') == 6
        assert response.response.get('total') == 12
        assert response.response.get('total_pages') == 2
        return response

    def test_get_single_resources_api(self, url):
        response = Resources(url).get_single_resource(schema=invalid_schema)
        assert response.status == 200
        assert response.response.get('data').get('id') == 2
        assert response.response.get('data').get('name') == 'fuchsia rose'
        assert response.response.get('data').get('year') == 2001
        assert response.response.get('data').get('color') == '#C74375'
        assert response.response.get('data').get('pantone_value') == '17-2031'
        assert response.response.get('support').get('text') == 'To keep ReqRes free, contributions towards server costs are appreciated!'
        assert response.response.get('support').get('url') == 'https://reqres.in/#support-heading'
        return response

    def test_single_resources_not_found_api(self, url):
        response = Resources(url).get_single_resource_not_found(schema=invalid_schema)
        assert response.status == 404
        return response
