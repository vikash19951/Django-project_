from django.shortcuts import render

# Create your views here.

def fee_courses(request):
    fee_details = {
        "Python_fee" : 3000,
        "Django_fee": 2000,
        "SQL_fee":2200
    }
    return render(request, 'fee/feeone.html', fee_details)
