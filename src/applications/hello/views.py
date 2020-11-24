from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def hello(request: HttpRequest) -> HttpResponse:
    result = render(request, "hello/hello.html")

    return HttpResponse(result)
