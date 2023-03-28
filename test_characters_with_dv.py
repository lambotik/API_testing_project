import requests

base_url = 'https://swapi.dev/api/'
get_resource_dv = 'people/4/'


class TestCharacters:
    def test_check_all_characters_with_dv(self):
        get_resource = requests.get(base_url + get_resource_dv)
        json_get_resource = get_resource.json()
        assert get_resource.status_code == 200, 'Bad response'  # Check status code
        print('Status code is: ', get_resource.status_code)
        assert json_get_resource.get(
            'name') == 'Darth Vader', 'Name is not Dart Vader'  # Check name character is Dart Vader
        print('Name character is: Dart Vader')
        list_films = get_resource.json().get('films')  # Get list all url films with Dart Vader
        print('Films with Dart Vader: ', list_films)
        list_characters_in_all_films = []
        '''Getting list all url characters in films with Dart Vader'''
        for film in list_films:
            if requests.get(film).json().get('characters') not in list_characters_in_all_films:
                list_characters_in_all_films.append(requests.get(film).json().get('characters'))
        list_without_duplicate = []
        '''The first loop goes through the list of all character urls in Darth Vader movies. 
        The second loop goes through each character url, gets its name, and if it does not repeat, 
        it writes it to the characters.txt file'''
        for characters in list_characters_in_all_films:
            for name in characters:
                name_character = requests.get(name).json().get('name')
                assert requests.get(name).status_code == 200, f'Bad status code for: {name}'
                if name_character not in list_without_duplicate:
                    list_without_duplicate.append(requests.get(name).json().get('name'))
                    file = open('characters.txt', 'a', encoding='utf-8')
                    file.write(name_character + '\n')
                    file.close()
        # print(f'List all characters: {list_without_duplicate}')
