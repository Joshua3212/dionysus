from src.app import App
from schema import Optional
from src.adapters.redis import RedisAdapter


r = RedisAdapter(
    redis_host="<host>",
    redis_port="<port>",
    redis_password="<pwd>",
    redis_username="<username>",
    channels=["test"],
)

"""
    You need to define an on_recv and on_send function.
    Feel free to write your own adapters. Check ./src/adapters/redis.py
"""


a = App(on_recv=r.on_data, on_send=r.on_send)


"""
    Schemata can be used to validate responses and replys
    (If faulty an invalid_data error will be sent.)
    This uses the schema package (https://pypi.org/project/schema/)
"""


data_schema = {"route": str, "req": dict, Optional("name"): str}
response_schema = {
    "a": str,
}


"""
    Functions can be triggered with an @app.on decorator.
"""


@a.on("/fake", schema=data_schema, response_schema=response_schema)
def reply_fake(data):
    print(data)
    return {"a": "b"}


"""
    Functions do not need to reply.
"""


@a.on("/some_enpoint", schema=data_schema)
def noreply_hey(data):
    print(data)


if __name__ == "__main__":
    a.start()
