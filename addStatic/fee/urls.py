from django.urls import path
from . import views
urlpatterns = [
    path('price/', views.omlete_price),
]
