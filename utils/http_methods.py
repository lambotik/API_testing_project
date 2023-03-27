import requests

'''List http methods'''
class HTTP_Methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result