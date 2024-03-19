from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def funciono(request):
    return HttpResponse("si funciono esta asdfsdfdre me gusto ")
