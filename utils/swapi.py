import allure

from utils.http_methods import HTTP_Methods

from utils.checking import Checking

base_url = 'https://swapi.dev/api/'
get_resource_dv = 'people/4/'


class SWAPI:

    @staticmethod
    @allure.step('checking_dart_vader_films')
    def checking_dart_vader_films():
        get_url = base_url + get_resource_dv
        print(get_url)
        result_get = HTTP_Methods.get(get_url)
        Checking.check_json_value(result_get, 'name', 'Darth Vader')
        return result_get

    '''Method get list films with DV'''

    @staticmethod
    @allure.step('get_list_films')
    def get_list_films():
        result_get = SWAPI.checking_dart_vader_films()
        Checking.check_status_code(result_get, 200)
        check_films = result_get.json()
        json_for_check_films = check_films.get('films')
        list_films = []
        for film in json_for_check_films:
            list_films.append(film)
        print(f'List films with Dart Vader: {list_films}')
        return list_films

    @staticmethod
    @allure.step('get_list_characters')
    def get_list_characters():
        films = SWAPI.get_list_films()
        list_characters = []
        url_dv = SWAPI.checking_dart_vader_films().json().get('url')
        for url in films:
            get_url = url
            print(get_url)
            result_get = HTTP_Methods.get(get_url)
            Checking.check_status_code(result_get, 200)
            if result_get not in list_characters:
                list_characters.append(result_get.json().get('characters'))
        new_list = []
        for i in list_characters:
            assert url_dv in i, f'{url_dv} is not present in: {i}'
            print(f'{url_dv} is present in {i}')
            for j in i:
                if j not in new_list:
                    get_url = j
                    result_get = HTTP_Methods.get(get_url)
                    print(j)
                    Checking.check_status_code(result_get, 200)
                    new_list.append(j)
        return new_list
