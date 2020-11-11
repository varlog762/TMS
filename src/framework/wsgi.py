from framework.errors import NotFound
from framework.types import RequestT
from framework.utils import build_form_data
from framework.utils import get_request_body
from framework.utils import get_request_headers
from framework.utils import get_request_method
from framework.utils import get_request_path
from framework.utils import get_request_query
from handlers import get_handler_and_kwargs
from handlers import special


def application(environ: dict, start_response):
    path = get_request_path(environ)
    method = get_request_method(environ)
    handler, kwargs = get_handler_and_kwargs(path)
    request_headers = get_request_headers(environ)
    query = get_request_query(environ)
    body = get_request_body(environ)
    form_data = build_form_data(body)

    request = RequestT(
        body=body,
        form_data=form_data,
        headers=request_headers,
        kwargs=kwargs,
        method=method,
        path=path,
        query=query,
    )

    try:
        response = handler(request)
    except NotFound:
        response = special.handle_404(request)
    except Exception:
        response = special.handle_500(request)

    start_response(response.status, list(response.headers.items()))

    yield response.payload or b""
