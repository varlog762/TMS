from framework.types import ResponseT
from framework.utils import read_static


def handle_logo(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "image/png"}
    payload = read_static("logo.png")

    return status, headers, payload
