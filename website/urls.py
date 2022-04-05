from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/docs", views.docs, name="docs"),
    path("api/", views.apis, name="apis"),
    path("api/private/", views.post_or_get, name="post_or_get"),
]
