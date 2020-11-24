from django.contrib import admin
from django.urls import path, include

from applications.landing.views import index

urlpatterns = [
    path("", index),
]
