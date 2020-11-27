from django.contrib import admin
from django.urls import include
from django.urls import path

from applications.landing.views import index

urlpatterns = [
    path("", index),
]
