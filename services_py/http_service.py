import requests
import json

class HTTPService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}/{endpoint}', params=params)
        return response.json()

    def post(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{self.base_url}/{endpoint}', data=json.dumps(data), headers=headers)
        return response.json()

    def put(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f'{self.base_url}/{endpoint}', data=json.dumps(data), headers=headers)
        return response.json()

    def patch(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(f'{self.base_url}/{endpoint}', data=json.dumps(data), headers=headers)
        return response.json()

    def delete(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(f'{self.base_url}/{endpoint}', data=json.dumps(data), headers=headers)
        return response.json()