from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    return render(request, 'course.html')

def learn_python(request):
    return HttpResponse('<h1>Hello Python<h1>')