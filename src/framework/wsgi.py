import mimetypes
import random

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    file_names = {
        "/styles.css": "styles.css",
        "/pic.png": "pic.png",
        "/test.pdf": "test.pdf",
        "/": "index.html",
    }

    file_name = file_names.get(url)
    if file_name is not None:
        status = "200 OK"
        headers = {
            "Content-type": mimetypes.guess_type(file_name)[0],
        }
        payload = read_static(file_name)
        start_response(status, list(headers.items()))
        yield payload
    else:
        status = "404 Not Found"
        headers = {
            "Content-type": "text/plain",
        }
        payload = error_404(url)
        start_response(status, list(headers.items()))
        yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name
    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def error_404(url: str) -> bytes:
    numb = random.randint(900, 999)
    payload = f"Your number is: {numb}. Page {url} not found!"

    return payload.encode('utf-8')

