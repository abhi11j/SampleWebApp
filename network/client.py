import requests

class NetworkClient:
    def get(self, url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)
