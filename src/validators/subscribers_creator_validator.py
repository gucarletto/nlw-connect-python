from cerberus import Validator

def subscribers_creator_validator(request: any):
    schema = {
        'name': {
            'type': 'string',
            'required': True,
            'empty': False
        },
        'email': {
            'type': 'string',
            'required': True,
            'empty': False
        },
        'evento_id': {
            'type': 'integer',
            'required': True,
            'empty': False
        },
        'link': {
            'type': 'string',
            'required': False,
            'empty': False
        }
    }
    v = Validator(schema)
    response = v.validate(request)
    if response is False:
        raise Exception(v.errors)