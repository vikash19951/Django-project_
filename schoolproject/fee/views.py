from django.shortcuts import render
from django.http import HttpResponse


def python_fee(request):
    return HttpResponse("Fee of python is 500 rupees")

def monthly_fee(request):
    return HttpResponse("<h1>MOnthly fee is :- 600 <h1>")