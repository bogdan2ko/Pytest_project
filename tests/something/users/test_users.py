from configuration import SERVICE_URL1

import requests
import pytest
from tests.src.baseclasses.response import Response
from src.pydantic_schemas.user import User

# resp= requests.get(url=SERVICE_URL1)


# print(resp.json())


# def test_getting_users_list(say_hello):
#     response = requests.get(SERVICE_URL1)
#     test_object = Response(response)
#     test_object.validate_status_code(200).validate(User)
#     print(say_hello)
    

@pytest.mark.development
@pytest.mark.production   
@pytest.mark.skip(reason="[ISSUE-2333] Issue with connecting to the database")
def test_another():
    assert 1 == 1 


@pytest.mark.production
def test_getting_users_list1(get_users, get_numbers, calculate, make_number):
    Response(get_users).validate_status_code(200).validate(User)
    # print(make_number)



@pytest.mark.development                   #D:\test_Py\tests\something\users\test_users.py -s -v -k development   or D:\test_Py\tests\something\users\test_users.py -s -v -k  " not development" для не отмеченых   
@pytest.mark.parametrize("first_value, second_value, expected",[
(1, 2, 3),
(-1,-3,-4),
(1,-3,-2),
(-1,3,2),
(1, "w", None),
("w", "r", None)
])    
def test_calculator(first_value, second_value, expected, calculate):
    assert calculate(first_value, second_value) == expected


@pytest.mark.development
@pytest.mark.production   
def test_another_faling():
    assert 1 == 2 
   


# {'meta': 
#  {'pagination': 
#   {'total': 2960, 'pages': 296, 'page': 1, 'limit': 10, 
#    'links': 
#    {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}},


# 'data': [{'id': 7834439, 'name': 'Mrs. Aslesha Malik', 'email': 'aslesha_mrs_malik@champlin.test', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834438, 'name': 'Lalita Saini', 'email': 'saini_lalita@rippin-parisian.example', 'gender': 'female', 'status': 'active'}, 
#          {'id': 7834437, 'name': 'Gajabahu Guneta', 'email': 'gajabahu_guneta@miller-runolfsdottir.test', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834436, 'name': 'Eshana Pandey', 'email': 'eshana_pandey@terry.example', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834435, 'name': 'Ujjawal Reddy', 'email': 'reddy_ujjawal@jenkins-deckow.test', 'gender': 'female', 'status': 'active'}, 
#          {'id': 7834434, 'name': 'Dron Butt', 'email': 'butt_dron@pfannerstill-dietrich.test', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834433, 'name': 'Harinakshi Kaul', 'email': 'harinakshi_kaul@casper.test', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834432, 'name': 'Acaryatanaya Abbott MD', 'email': 'md_abbott_acaryatanaya@barton-bogan.example', 'gender': 'male', 'status': 'inactive'}, 
#          {'id': 7834430, 'name': 'Prasanna Chopra', 'email': 'prasanna_chopra@walsh.test', 'gender': 'male', 'status': 'active'}, 
#          {'id': 7834429, 'name': 'Jitendra Gowda DC', 'email': 'jitendra_gowda_dc@satterfield-goodwin.test', 'gender': 'female', 'status': 'active'}]} 


# pytest D:\test_Py\tests\something\users\test_users.py -s -v --durations=3 -vv  для отображения самх долгих этапов тестирования функции