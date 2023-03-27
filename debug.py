import requests

base_url = 'https://swapi.dev/api/'
get_resource_dv = 'people/4/'

class TestCharacters:
    def check_all_characters_with_dv(self):
        get_resource = requests.get(base_url + get_resource_dv)
        json_get_resource = get_resource.json()
        assert get_resource.status_code == 200, 'Bad response'
        assert json_get_resource.get('name') == 'Darth Vader', 'Name is not Dart Vader'
        print(json_get_resource)
        list_films = get_resource.json().get('films')
        print('Films with Dart Vader: ', list_films)
        list_characters_in_all_films = []
        for film in list_films:
            if requests.get(film).json().get('characters') not in list_characters_in_all_films:
                list_characters_in_all_films.append(requests.get(film).json().get('characters'))
        list_without_duplicate = []
        for characters in list_characters_in_all_films:
            for name in characters:
                if name not in list_without_duplicate:
                    list_without_duplicate.append(requests.get(name).json().get('name'))
        print(list_without_duplicate)




a = TestCharacters()
a.check_all_characters_with_dv()