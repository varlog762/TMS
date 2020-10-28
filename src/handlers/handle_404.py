import random

from framework.types import ResponseT


def handle_404(environ) -> ResponseT:
    status = "404 Not Found"
    headers = {"Content-type": "text/html"}

    numb = random.randint(900, 999)
    payload = f"Your number is: {numb}. Page  not found!"

    return status, headers, payload.encode("utf-8")
