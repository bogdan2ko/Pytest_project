from pydantic import BaseModel, validator , Field


class Post(BaseModel):
    id: int = Field(gt=0)
    title: str 
    # name: str = Field(alias="_name")

    # @validator("id")
    # def check_id(cls, v):
    #     if v > 2:
    #         raise ValueError("ID must be a > 2")
    #     else:
    #         return v


 # [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]