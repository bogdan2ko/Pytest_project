import requests

from src.baseclasses.response import Response
from jsonschema import validate
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessage
# from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post
from configuration import SERVICE_URL

def test_getting_posts():
    r= requests.get(url=SERVICE_URL)
    response = Response(r)


    received_posts = response.response_json
    print(received_posts)

    response.validate_status_code(200).validate(Post)

    # [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]