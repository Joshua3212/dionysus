"""
    A dummy adapter getting data every second and sending it nowhere
"""


class RedisAdapter:
    def __init__(self):
        pass

    def on_data(self, callback):
        for _i in range(1, 100):
            print("-- dummy adapter on_data")
            callback("/dummy", {"a": "b", "b": {"c": "d"}})

    def on_send(self, data):
        print("-- dummy adapter on_send")
        print(data)