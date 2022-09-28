from django.urls import path
from .views import main

urlpatterns = [
    path('', main, name='main_view'),
]
