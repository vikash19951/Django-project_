from django.urls import path
from . import views 
urlpatterns = [
    path('fee/', views.monthly_fee, name='monhtly-fee'),
    path('pythonfee/', views.python_fee)
]
