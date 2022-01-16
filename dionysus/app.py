import asyncio

from .utils.errors import invalid_payload, invalid_response
from .utils.schemata import validate_schema


class App:
    def __init__(self, on_recv, on_send, response_template={}):
        self.on_send = on_send
        self.on_recv = on_recv
        self.response_template = response_template
        self.indentifiers = []

    def on(self, indentifier, schema=None, response_schema=None, **kwargs):
        # save all function in identifiers list
        def wrapper(func, **kwargs):
            self.indentifiers.append(
                {
                    "indentifier": indentifier,
                    "func": func,
                    "schema": schema,
                    "response_schema": response_schema,
                }
            )

        return wrapper

    def start(self):
        # start receiving data using the given adapter
        self.on_recv(self.run)

    def execute_function(self, func, data):
        # check if function is async function; then run correspondingly
        if asyncio.iscoroutinefunction(func):
            return asyncio.run(func(data))
        else:
            return func(data)

    def run(self, indentifier, data):
        item = [
            item for item in self.indentifiers if item["indentifier"] == indentifier
        ]
        if len(item) == 1:
            # validate payload and run function
            try:
                if item[0]["schema"]:
                    payload = validate_schema(item[0]["schema"], data)
                else:
                    payload = data

                response = self.execute_function(item[0]["func"], payload)
            except:
                # if validation fails don't run the function; instead return invalid_payload error
                response = invalid_payload()

            if not response == invalid_payload():
                if item[0]["response_schema"]:
                    try:
                        response = validate_schema(item[0]["response_schema"], response)
                    except:
                        # return invalid_response if validation of response fails. (prevent returning of senstive data)
                        response = invalid_response()
                else:
                    response = response
            # send data using the given adapter
            self.on_send(
                {**self.response_template, **response}
            )  # merge response_template with response (response can override response_template)
