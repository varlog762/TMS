from handlers.handle_404 import handle_404
from handlers.handle_index import handle_index
from handlers.handle_css import handle_css
from handlers.handle_logo import handle_logo
from handlers.handle_pdf import handle_pdf

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


