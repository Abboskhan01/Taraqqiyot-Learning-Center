from django.urls import path
from .views import main,register
urlpatterns = [
    path('', main, name='main'),
    path('reg/',register, name='reg')
]