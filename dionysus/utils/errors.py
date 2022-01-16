def invalid_payload():  # used in ..app.py
    return {
        "msg": "The data you sent appears to be invalid.",
        "code": "INVALID_PAYLOAD",
    }


def invalid_response():  # used in ..app.py
    return {
        "msg": "The server sent an invalid response.",
        "code": "INVALID_RESPONSE",
    }


def auth_required():
    return {
        "msg": "You need to be authenticated to access this resource.",
        "code": "AUTH_REQUIRED",
    }


def not_found():
    return {"msg": "The data you tried to access was not found.", "code": "NOT_FOUND"}
