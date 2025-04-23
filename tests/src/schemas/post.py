POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'title': {'type': 'string', "enum": ["Post 2", "Post 1", "Post 3"]},
    
    },
    "required": ['id']


}


# {'id': 1, 'title': 'Post 1'}