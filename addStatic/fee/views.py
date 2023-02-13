from django.shortcuts import render

# Create your views here.

def omlete_price(request):
    return render(request, 'fee/feeone.html', {"normal_oml":30, "Pudin_oml": 50, "Dhania_oml":50, "hm_oml":450})
    
