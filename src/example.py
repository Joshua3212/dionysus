from utils.app import App
from schema import Optional
from adapters.redis import RedisAdapter


fuck = RedisAdapter(
    redis_host="host",
    redis_port="port",
    redis_password="pwd",
    redis_username=None,
    channels=["test"],
)


a = App(on_recv=fuck.on_data, on_send=fuck.on_send)


data_schema = {"route": str, "req": dict, Optional("name"): str}

response_schema = {
    "a": str,
}


@a.on("/fake", schema=data_schema, response_schema=response_schema)
def reply_fake(data):
    print(data)
    return {"a": "b"}


@a.on("/hey", schema=data_schema)
def noreply_hey(data):
    print(data)


if __name__ == "__main__":
    a.start()
