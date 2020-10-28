from framework.wsgi import read_static
from framework.wsgi import ResponseT


def handle_css(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "text/css"}
    content = read_static("styles.css")

    return status, headers, content
