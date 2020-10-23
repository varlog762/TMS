import mimetypes

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]
    dot = "."
    if dot in url:
        m_type = mimetypes.guess_type(url)
    else:
        m_type = ("text/html",)
        """Проверяем содержится ли в урле запроса точка: если да, то тип контента определяет mimetypes, 
        если нет, значит зпрашивается / и выставляется тип 'text/html'."""

    if url == "/styles.css":
        status = "200 OK"
        headers = {
            "Content-type": m_type[0],
        }
        payload = read_from_styles_css()
        start_response(status, list(headers.items()))

        yield payload
    elif url == "/pic.png":
        status = "200 OK"
        headers = {
            "Content-type": m_type[0],
        }
        payload = read_from_png()
        start_response(status, list(headers.items()))

        yield payload
    elif url == "/test.pdf":
        status = "200 OK"
        headers = {
            "Content-type": m_type[0],
        }
        payload = read_from_pdf()
        start_response(status, list(headers.items()))
    else:
        status = "200 OK"
        headers = {
            "Content-type": m_type[0],
        }
        payload = read_from_ind_html()

        start_response(status, list(headers.items()))

        yield payload


def read_from_ind_html():
    path = DIR_STATIC / "index.html"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    # str.encode() - рекодирует строку в байтстроку
    return payload


def read_from_styles_css():
    path = DIR_STATIC / "styles.css"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_png():
    path = DIR_STATIC / "pic.png"
    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def read_from_pdf():
    path = DIR_STATIC / "test.pdf"
    with path.open("rb") as fp:
        payload = fp.read()

    return payload
