from django.urls import path
from . import views
urlpatterns = [
    path('learnpython/', views.python_fee),
    path('learndjango/', views.django_fee),
]
