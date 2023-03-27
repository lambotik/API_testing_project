"""Methods for checking requests"""
import json


class Checking:
    """Method for checking status code"""

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'Incorrect status code'
        print(f'Successfully!!! Status code is: {result.status_code}')

    """Method for validating fields in a response"""

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        """list(token) generated list of keys from json"""
        assert list(token) == expected_value, 'Not all fields are presented'
        print('All fields is present')

    """Method for checking values of required fields in response"""

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'Result is not equal expected value'
        print(f'{field_name}: {expected_value}: is correct')

    """Method for checking values of required fields in response by word"""

    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Word: {search_word}, is present in: {field_name}')
        else:
            print(f'Word: {search_word} is not present in: {field_name}')
