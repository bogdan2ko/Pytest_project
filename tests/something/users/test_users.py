from configuration import SERVICE_URL1

import requests
import pytest
from tests.src.baseclasses.response import Response
from tests.src.pydantic_schemas.user import User
from tests.src.generators.player_localization import PlayerLocalization
from tests.src.pydantic_schemas.computer import Computer
from tests.src.pydantic_schemas.computer import computer
from tests.src.enums.user_enums import Status


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
    print(get_numbers)



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



#  _______________________________________________________________________________________________________________________________________________________________________________________________________   


@pytest.mark.parametrize("status", 
Status.list()
)
def test_something(status, get_player_generator):
    """
    In that test we try chek the parametrization of player generator

    """
    print(get_player_generator.set_status(status).build())




# @pytest.mark.parametrize("balance_value", 
# ["100", "0", "-10", "asd"]
# )
# def test_something1(balance_value, get_player_generator):
#     """
#     In that test we try chek the parametrization of player generator

#     """
#     print(get_player_generator.set_balance(balance_value).build())




# @pytest.mark.parametrize("delete_key", 
# ["account_status", "balance", "localization", "avatar"]
# )
# def test_something2(delete_key, get_player_generator):
#     object_to_delete = get_player_generator.build()
#     del object_to_delete[delete_key]
#     print(object_to_delete)



@pytest.mark.parametrize("localize, loc",  [("fr","fr_FR") ])
def test_something3(get_player_generator, localize, loc):
    
    object_to_send = get_player_generator.update_inner_value(["localization", localize], PlayerLocalization(loc).set_number(15).build()).build()
    
    # Print the updated object
    print(object_to_send)




def test_pydantic_object():
    """
    In that test we try to check the pydantic object with the help of the response class

    """
    comp = Computer.model_validate(computer)
    # print(comp.detailed_info.physical.color.as_rgb())
    print(comp.model_json_schema())


