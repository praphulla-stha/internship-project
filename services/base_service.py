import requests
from utils.request import make_request

class BaseService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        return make_request("GET", f"{self.base_url}/{endpoint}", params=params)

    def post(self, endpoint, data=None):
        return make_request("POST", f"{self.base_url}/{endpoint}", json=data)

    def put(self, endpoint, data=None):
        return make_request("PUT", f"{self.base_url}/{endpoint}", json=data)

    def delete(self, endpoint):
        return make_request("DELETE", f"{self.base_url}/{endpoint}")