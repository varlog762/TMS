from django.contrib import admin
from django.urls import path, include

from applications.hello.views import hello

urlpatterns = [
    path("", hello,)
]