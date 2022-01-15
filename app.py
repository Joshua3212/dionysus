import asyncio

from utils.schemata import validate_schema


class App:
    def __init__(self, on_recv, on_send):
        self.on_send = on_send
        self.on_recv = on_recv
        self.routes = []

    def on(self, route, schema=None, response_schema=None, **kwargs):
        def wrapper(func, **kwargs):
            self.routes.append(
                {
                    "route": route,
                    "func": func,
                    "schema": schema,
                    "response_schema": response_schema,
                }
            )

        return wrapper

    def start(self):
        self.on_recv(self.run)

    def execute_function(self, func, data):
        if asyncio.iscoroutinefunction(func):
            return asyncio.run(func(data))
        else:
            return func(data)

    def run(self, route, data):
        for item in self.routes:
            if item["route"] == route:
                # validate payload and run function
                if item["schema"]:
                    payload = validate_schema(item["schema"], data)
                else:
                    payload = data

                response = self.execute_function(item["func"], payload)

                if item["response_schema"]:
                    response = validate_schema(item["response_schema"], response)
                else:
                    response = response
                self.on_send(response)