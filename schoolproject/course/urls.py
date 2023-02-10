from django.urls import path
from . import views 


urlpatterns = [
    path('learndjango/', views.learn_django),
    path('leanpython/',views.learn_python ),
    path('',views.default),
]
