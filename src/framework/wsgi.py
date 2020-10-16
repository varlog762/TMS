from framework.consts import DIR_STATIC


def application(environ, start_response):
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = read_from_ind_html()

    start_response(status, list(headers.items()))

    yield payload


def read_from_ind_html():
    path = DIR_STATIC / "index.html"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    # str.encode() - перекодирует строку в байтстроку
    return payload
