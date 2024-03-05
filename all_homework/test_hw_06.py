import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"

@pytest.fixture(scope='module')
def auth_token():
   authdata = {
       "username": "admin",
       "password": "password123"
   }
   response = requests.post(auth_url, json=authdata)
   token = response.json()["token"]
   yield token


@pytest.fixture(scope="session")
def booking_id():
   payload = {
       "firstname": "James",
       "lastname": "Brown",
       "totalprice": 150,
       "depositpaid": True,
       "bookingdates": {
           "checkin": "2024-01-01",
           "checkout": "2024-02-01"
       },
       "additionalneeds": "Breakfast"
   }
   response = requests.post(base_url, json=payload)
   yield response.json()['bookingid']


# def sum_it(x, y):
#     return x + y
#
# def test_equal():
#     assert sum_it(5, 3) == 8
#
# def test_not_equal():
#     assert sum_it(4, 8) == 11

@pytest.mark.smoke
def test_get_code():
   result = requests.get(base_url)
   print(result)
   assert result.status_code == 200

@pytest.mark.skip
def test_get_booking_by_id():
   response = requests.get(f'{base_url}/1')
   response_data = response.json()
   expected_keys = [
       "lastname",
       "totalprice",
       "depositpaid",
       "bookingdates",
       "additionalneeds"
   ]
   assert response.status_code == 200
   print(response_data)
   print(len(response_data.keys()))
   assert len(response_data.keys()) == len(expected_keys)
   # for key in expected_keys:
   #     assert key in response_data.keys()


# def test_create_booking(booking_id):
#     response = requests.post(base_url,json=payload)
#     print(response.json()['bookingid'])
#     assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.xfail(reason='wrong status code')
def test_check_created_booking(booking_id):
   result = requests.get(f"{base_url}/{booking_id}")
   print(result.json())
   assert result.status_code == 200
   assert result.json()['firstname'] == "James"


def test_update_booking(auth_token, booking_id):
   payload = {
       "firstname": "James",
       "lastname": "Brown",
       "totalprice": 150,
       "depositpaid": False,
       "bookingdates": {
           "checkin": "2024-01-01",
           "checkout": "2024-02-01"
       },
       "additionalneeds": "Lunch"
   }
   token = {"Cookie": f"token={auth_token}"}

   response = requests.put(f'{base_url}/{booking_id}', json=payload, headers=token)
   assert response.status_code == 200
   response_2 = requests.get(f'{base_url}/{booking_id}')
   print(response_2.json())
   assert response_2.json()["additionalneeds"] == "Lunch"

def test_delete_booking(booking_id, auth_token):
   token = {"Cookie": f"token={auth_token}"}
   response = requests.delete(f'{base_url}/{booking_id}', headers=token)
   assert response.status_code == 201
   response_get = requests.get(f'{base_url}/{booking_id}')
   assert response_get.status_code == 404



# 1. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
def test_patch_booking(auth_token, booking_id):
   # Изменить имя, цену и дату выезда
   payload = {
       "firstname": "John",
       "totalprice": 200,
       "bookingdates": {
           "checkout": "2024-02-15"
       }
   }
   token = {"Cookie": f"token={auth_token}"}
   response = requests.patch(f'{base_url}/{booking_id}', json=payload, headers=token)
   assert response.status_code == 200

# 2. Проверить, что изменения применились
def test_verify_patch_booking(booking_id):
   response = requests.get(f'{base_url}/{booking_id}')
   assert response.status_code == 200
   response_data = response.json()
   # Проверить, что имя, цена и дата выезда соответствуют новым значениям
   assert response_data["firstname"] == "John"
   assert response_data["totalprice"] == 200
   assert response_data["bookingdates"]["checkout"] == "2024-02-15"