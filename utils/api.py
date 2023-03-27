import requests

from utils.http_methods import HTTP_Methods

"""Methods for testing Googlemaps api"""

base_url = 'https://rahulshettyacademy.com'  # Base url
key = '?key=qaclick123'


class GoogleMapsAPI:
    """Method for create new location"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {"location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"}

        post_resource = '/maps/api/place/add/json'  # Resource for method POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HTTP_Methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Method for checking new location"""

    @staticmethod
    def checking_new_place(place_id):
        get_resource = '/maps/api/place/get/json'  # Resource for method GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = HTTP_Methods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for changing new location"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = '/maps/api/place/update/json'  # Resource for method PUT
        put_url = base_url + put_resource + key + '&place_id='
        print(put_url)
        json_for_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HTTP_Methods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put

    """Method for delete new location"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = '/maps/api/place/delete/json'  # Resource for method DELETE
        delete_url = base_url + delete_resource + key + '&place_id=' + place_id
        print(delete_url)
        json_for_delete_new_place = {"place_id": place_id}
        result_delete = HTTP_Methods.delete(delete_url, json_for_delete_new_place)
        print(result_delete.text)
        return result_delete