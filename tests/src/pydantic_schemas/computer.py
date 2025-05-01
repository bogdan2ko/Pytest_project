from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Address, IPv6Address
from tests.src.pydantic_schemas.detail_info import DetailedInfo
from tests.src.enums.user_enums import Status



class Computer(BaseModel): 
    id: int
    status: Status
    activated_at: PastDate
    experation_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info:DetailedInfo




computer = {
    'id': 11,
    "status": "active",
    "activated_at": "2013-06-01",
    "experation_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0008:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": "green",
            "photo": "https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwZWYy2h8MXx8ZGVza3RvcuUyMGNvbXB1dGVyfDB8fDB8fA%3D%3D",
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [   # <<<< Переносим сюда owners
            {
                "name": "Stephan Nollan",
                "card_number": "4000000000000002",
                "email": "stephan.nollan@gmail.com"
            }
        ]
    }
}
comp = Computer.model_validate(computer)
print(comp)