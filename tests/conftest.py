import pytest
from random import randrange


@pytest.fixture
def get_numbers():
    return randrange(1,1000,5)



def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else: None

    

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    # print("Iam getting number")  #print bedore yeld 
    number = randrange(1,1000,5)
    yield number
    # print (f"Number at the end is {number}")