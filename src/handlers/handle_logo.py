from framework.wsgi import read_static
from framework.wsgi import ResponseT


def handle_logo(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "image/png"}
    payload = read_static("pic.png")

    return status, headers, payload
