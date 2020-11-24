from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "landing/index.html")

    return HttpResponse(result)