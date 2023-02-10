from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("<h1>Hello World<h1>")
    
def learn_python(request):
    a = "Python has wide uses in Data Science  Data Engineering and so on."
    return HttpResponse(f"<h2>Learn Python:{a}<h2>")

def learn_spark(requests):
    var = "You have to learn spark because it's faster than hadoop"
    return HttpResponse(f"Spark is :- {var}")

def default(request):
    return HttpResponse("If Nothing then learn SQL")