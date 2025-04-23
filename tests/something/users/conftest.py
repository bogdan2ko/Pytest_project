import pytest
from configuration import SERVICE_URL1

import requests

@pytest.fixture(scope="session")    #Session scope means the fixture is created once per test session  #function every time the test function is called 
def get_users():
    response = requests.get(SERVICE_URL1)
    return response 