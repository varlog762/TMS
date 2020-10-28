from framework.types import ResponseT
from framework.utils import read_static


def handle_css(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "text/css"}
    payload = read_static("styles.css")

    return status, headers, payload
