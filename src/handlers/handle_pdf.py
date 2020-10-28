from framework.types import ResponseT
from framework.utils import read_static


def handle_pdf(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "application/pdf"}
    content = read_static("test.pdf")

    return status, headers, content
