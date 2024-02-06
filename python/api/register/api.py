import logging
from jsonschema import validate

from python.api.register.requests import Client
from python.api.register.models import ResponseModel

logger = logging.getLogger("api")


class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = '/api/register'

    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class Login:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_LOGIN = '/api/register'

    def login_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.POST_LOGIN}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class Users:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    GET_LIST_USERS = '/api/users?page=2'
    GET_SINGLE_USER = '/api/users/2'
    GET_SINGLE_USER_NOT_FOUND = '/api/users/23'

    def get_list_users(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_LIST_USERS}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_single_users(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_SINGLE_USER}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_single_users_not_found(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_SINGLE_USER_NOT_FOUND}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class Resources:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    GET_LIST_RESOURCES = '/api/unknown'
    GET_SINGLE_RESOURCE = '/api/unknown/2'
    GET_SINGLE_RESOURCE_NOT_FOUND = '/api/unknown/23'

    def get_list_resources(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_LIST_RESOURCES}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_single_resource(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_SINGLE_RESOURCE}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_single_resource_not_found(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_SINGLE_RESOURCE_NOT_FOUND}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class CRUD:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_CREATE = '/api/users'
    PUT_UPDATE = '/api/users/2'
    PATCH_UPDATE = '/api/users/2'
    DELETE = '/api/users/2'

    def create(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.POST_CREATE}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def put_update(self, body: dict, schema: dict):
        response = self.client.custom_request("PUT", f"{self.url}{self.PUT_UPDATE}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def patch_update(self, body: dict, schema: dict):
        response = self.client.custom_request("PATCH", f"{self.url}{self.PATCH_UPDATE}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def delete(self, schema: dict):
        response = self.client.custom_request("DELETE", f"{self.url}{self.DELETE}")
        if response.status_code == 204:
            return response.status_code
        else:
            validate(instance=response.json(), schema=schema)
            logger.info(response.text)
            return ResponseModel(status=response.status_code, response=response.json())


class Delay:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    GET_DELAYED_RESPONSE = "/api/users?delay=3"

    def get_delayed_response(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_DELAYED_RESPONSE}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
