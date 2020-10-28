from framework.wsgi import read_static
from framework.wsgi import ResponseT


def handle_index(_environ) -> ResponseT:
    status = "200 OK"
    headers = {"Content-type": "text/html"}
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    payload = base_html.format(page=index_html)

    return status, headers, payload.encode()
