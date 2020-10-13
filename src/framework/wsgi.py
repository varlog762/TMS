def application(environ, start_response):
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = b"""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Z37 Hello World!</title>
        <meta charset="utf-8">
        </head>
        <body>
        <h1>Z37 study project</h1>
        <h2>123456</h2>
        <h3>123456</h3>
        <hr>
        <p>This is a study project.</p>
        <p>This is a first project.</p>
        </body>
        </html>
    """


    start_response(status, list(headers.items()))

    yield payload
