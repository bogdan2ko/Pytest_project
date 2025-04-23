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
    """
    In that test we try to check than 1 is equal to 2 

    """
    assert 1 == 1 


@pytest.mark.production
def test_getting_users_list1(get_users, get_numbers, calculate, make_number):
    """
    In that test we try to connet to endpoint and get the list with information about users
    
    """
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
    """
    In that test we teasting calculating function with different values

    """
    assert calculate(first_value, second_value) == expected


@pytest.mark.development
@pytest.mark.production   
def test_another_faling():
    """
    In that test we try to check than 1 is equal to 2 , but with the different marks 

    """
    assert 1 == 2 
   

