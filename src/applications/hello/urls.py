from django.contrib import admin
from django.urls import include
from django.urls import path

from applications.hello.views import view_hello_greet
from applications.hello.views import view_hello_index
from applications.hello.views import view_hello_reset

urlpatterns = [
    path("", view_hello_index),
    path("greet/", view_hello_greet),
    path("reset/", view_hello_reset),
]
