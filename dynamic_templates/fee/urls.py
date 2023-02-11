from django.urls import path, include
from . import views
urlpatterns = [
    path('feedetails/',views.fee_courses)
]
