from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("applications.landing.urls")),
    path("h/", include("applications.hello.urls")),
    path("admin/", admin.site.urls),
]
