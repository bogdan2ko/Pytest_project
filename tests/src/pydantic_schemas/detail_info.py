from pydantic import BaseModel
from typing import List
from tests.src.pydantic_schemas.physical import Physical
from tests.src.pydantic_schemas.owner import Owners




class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]
