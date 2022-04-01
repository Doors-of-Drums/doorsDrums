from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/docs", views.docs, name="docs"),
    path("api/", views.apis, name="apis"),
]
