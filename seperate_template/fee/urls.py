from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('djangofee/', views.django_fee),
    path('pythonfee/', views.python_fee)
]
