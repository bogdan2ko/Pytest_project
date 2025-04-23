
from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessage



class Response:
    """
    Base class for all response classes.
    """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.status_code = response.status_code
        
    def validate(self, schema):
        if isinstance(self.response_json, list):  # Проверка на список
            for item in self.response_json:
                schema.model_validate(item)  # Валидация каждого элемента списка
        else:
            schema.model_validate(self.response_json)  # Валидация одного объекта
        return self
    


    def validate_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.status_code in expected_status_code, self
        else:
            assert self.status_code == expected_status_code, self
        return self
    
    def __str__(self):
        return (
            f"\n Status Code: {self.status_code},"
            f"\n Request URL: {self.response.url},"
            f"\n Respone body: {self.response_json},"
        )
