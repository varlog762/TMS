from typing import Tuple

from framework.consts import DIR_STATIC
from handlers.handle_404 import handle_404

ResponseT = Tuple[str, dict, bytes]

handlers = {
    "/": handle_index,
    "/pic.png": handle_logo,
    "/styles.css": handle_css,
    "/test.pdf": handle_pdf,
}


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handler = handlers.get(url, handle_404)

    status, headers, payload = handler(environ)

    start_response(status, list(headers.items()))

    yield payload


def read_static(file_name) -> bytes:
    path = DIR_STATIC / file_name
    with path.open("rb") as fp:
        payload = fp.read()

    return payload
