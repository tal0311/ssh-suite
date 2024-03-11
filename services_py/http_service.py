import requests
import json

class HTTPService:
    def __init__(self, base_url):
        self.base_url = 'http://127.0.0.1:1337'+ base_url

    def get(self, endpoint, params=None):
        print(f'{self.base_url}/{endpoint}')
        response = requests.get(f'{self.base_url}/{endpoint}', params=params)
        return response.json()

    def post(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        print(f'{self.base_url}/{endpoint}')
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
    


auth_http = HTTPService('/api/auth')
res= auth_http.post('signin', {'username': 'admin', 'password': 'admin'})
print(res)