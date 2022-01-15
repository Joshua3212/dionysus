from schema import Schema


def validate_schema(schema, data):
    return Schema(schema).validate(data)


def is_schema_valid(schema, data):
    return Schema(schema).is_valid(data)