from src.app import App
from schema import Optional

# from src.adapters.redis import RedisAdapter
from src.adapters.dummy import DummyAdapter


"""
    How to - Redis Adapter :
"""
# r = RedisAdapter(
#    redis_host="<host>",
#    redis_port="<port>",
#    redis_password="<pwd>",
#    redis_username="<username>",
#    channels=["test"],
# )

"""
    How to - Dummy Adapter:
"""

d = DummyAdapter()

"""
    You need to define an on_recv and on_send function.
    Feel free to write your own adapters. Check ./src/adapters/redis.py
"""

"""
    The RedisAdapter class emits the exact same functions as the DummyAdapter for on_recv and on_send:
"""
# a = App(on_recv=r.on_data, on_send=r.on_send)
a = App(on_recv=d.on_data, on_send=d.on_send)

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


@a.on("/dummy", schema=data_schema, response_schema=response_schema)
def reply_dummy_adapter(data):
    print(data)
    return {"a": "b"}


"""
    Functions do not need to return anything.
"""


@a.on("/some_other_endpoint", schema=data_schema)
def noreply(data):
    print(data)


if __name__ == "__main__":
    a.start()
