from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Usuario


def index(response):
    return HttpResponse("<h1>Hello</h1>")


def docs(response):
    return HttpResponse("<h1>Docs site UwU<h1>")


def apis(response):
    user_list = serializers.serialize('json', Usuario.objects.all())
    return HttpResponse(user_list, content_type="text/users.json")
