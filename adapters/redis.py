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
            print(item)
            if item["data"] == b"KILL":
                """
                KILL service if kill signal is emited
                """
                self.pubsub.unsubscribe()
                print("-- unsubscribed")
                break
            else:
                try:
                    data = json.loads(item["data"])
                except:
                    data = {"data": item["data"]}
                if not "route" in data:
                    data["route"] = ""
                callback(data["route"], data)

    def on_send(self, data):
        for channel in self.channels:
            self.redis.publish(channel, json.dumps(data))
