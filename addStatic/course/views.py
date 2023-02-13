from django.shortcuts import render

# Create your views here.


def learn_django(request):
    return render(request,'course/courseone.html', {'Title': 'Furki kutta hai', 'cname': "Omlete me Hagal mutal dalta hai"})