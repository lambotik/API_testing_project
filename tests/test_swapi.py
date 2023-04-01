import json

import allure

from utils.checking import Checking
from utils.http_methods import HTTP_Methods
from utils.swapi import SWAPI


@allure.feature('Test Swapi')
class TestSwapi:
    @allure.step('test_all_films_with_DV')
    def test_all_films_with_DV(self):
        list_characters = SWAPI.get_list_characters()
        for character in list_characters:
            get_result = HTTP_Methods.get(character)
            name = get_result.json().get('name')
            file = open('characters1.txt', 'a', encoding='utf-8')
            file.write(f'{name}\n')
            file.close()
