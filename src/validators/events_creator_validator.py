from cerberus import Validator

def events_creator_validator(request: any):
    schema = {
        'name': {
            'type': 'string',
            'required': True,
            'empty': False
        }
    }
    v = Validator(schema)
    response = v.validate(request)
    if response is False:
        raise Exception(v.errors)