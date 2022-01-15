from utils.app import App
from schema import Optional
from adapters.redis import RedisAdapter


fuck = RedisAdapter(
    redis_host="redis-11513.c92.us-east-1-3.ec2.cloud.redislabs.com",
    redis_port="11513",
    redis_password="ypnGgkYYfrafhbBnbu5vCYZhz5H5OqL0",
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