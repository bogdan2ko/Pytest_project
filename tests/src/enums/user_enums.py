from enum import Enum
from tests.src.baseclasses.pyenum import PyEnum


class Gender(Enum):
    female ="female"
    male = "male"

class Status(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    DELETED = "deleted"
    MERGED = "merged"

class UserErrors(Enum):
    WRONG_EMAIL = "Email must contain '@'"

print(Status.list())