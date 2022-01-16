import json, redis, time


class RedisAdapter:
    def __init__(
        self, redis_host, redis_port, redis_password, redis_username, channels
    ):
        self.redis = redis.Redis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            username=redis_username,
        )
        time.sleep(1)
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
        self.channels = channels

    def on_data(self, callback):
        for item in self.pubsub.listen():
            print(f"{int(time.time())} -- got data -- {item['data']}")
            # KILL service if kill signal is emited
            if item["data"] == b"KILL":
                self.pubsub.unsubscribe()
                print("-- got KILL signal")
                break
            else:
                try:
                    data = json.loads(item["data"])
                except:
                    data = {"data": item["data"]}
                if not "indentifier" in data:
                    data["indentifier"] = ""
                callback(data["indentifier"], data)

    def on_send(self, data):
        for channel in self.channels:
            print(f"{int(time.time())} -- sent data -- {data}")
            self.redis.publish(channel, json.dumps(data))
