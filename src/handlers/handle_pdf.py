from framework.wsgi import read_static
from framework.wsgi import ResponseT


def handle_pdf(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "application/pdf"}
    content = read_static("test.pdf")

    return status, headers, content
