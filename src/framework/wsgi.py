def application(environ, start_response):
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    # payload = read_from_ind_html()

    # --------------------------------------------
    path = "src/static/index.html"
    fp = open(path, "r")
    payload = fp.read()
    fp.close()

    payload = payload.encode()
    # --------------------------------------------


    start_response(status, list(headers.items()))

    yield payload
