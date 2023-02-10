from django.shortcuts import render

# Create your views here.

def python_fee(request):
    return render(request, 'fee/feeone.html')

def django_fee(request):
    return render(request, 'fee/feetwo.html')