from enum import Enum


class GlobalErrorMessage(Enum):
    """Global error messages."""
    WRONG_STATUS_CODE = "Expected status code not equal {status_code}"
    INVALID_INPUT = "Invalid input provided."
    NOT_FOUND = "The requested resource was not found."
    UNAUTHORIZED = "You are not authorized to perform this action."
    FORBIDDEN = "Access to the requested resource is forbidden."
    INTERNAL_SERVER_ERROR = "An internal server error occurred."
    BAD_REQUEST = "The request could not be understood or was missing required parameters."
    WRONG_ELEMENTS_IN_LIST = "Expected {expected} elements in the list, got {actual}."