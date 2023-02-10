from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def python_fee(request):
    return HttpResponse('<h1>300<h1>')

def django_fee(request):
    return HttpResponse('<h1>500<h1>')