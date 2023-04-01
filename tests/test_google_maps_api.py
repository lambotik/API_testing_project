import json

import allure

from utils.checking import Checking

from utils.api import GoogleMapsAPI

"""Create, edit and delete a new location"""


@allure.feature('Test Create Place')
class TestCreatePlace:
    @allure.step('test_create_new_place')
    def test_create_new_place(self):
        print('\nMethod POST')
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_value(result_post, 'status', 'OK')

        print('\nMethod GET POST')
        result_get = GoogleMapsAPI.checking_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number',
                                               'address', 'types', 'website', 'language'])
        print(list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('\nMethod PUT')
        result_put = GoogleMapsAPI.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('\nMethod GET PUT')
        result_get = GoogleMapsAPI.checking_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number',
                                               'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('\nMethod DELETE')
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('\nMethod GET DELETE')
        result_get = GoogleMapsAPI.checking_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'place_id')

        print('\nTesting of creating, editing and deleting a new location was successfully completed')
