import allure
import requests

from utils.logger import Logger

'''List http methods'''


class HTTP_Methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    @allure.step('Method GET')
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method POST')
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method PUT')
    def put(url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method DELETE')
    def delete(url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        Logger.add_response(result)
        return result
