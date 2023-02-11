from django.shortcuts import render

# Create your views here.
def learn_django(request):
    
    return render(request, 'course/courseone.html', context={'nm':'Django', 'st':10, 'price':2900 })