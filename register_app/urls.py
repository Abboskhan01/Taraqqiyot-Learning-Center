from django.urls import path
from .views import regiter_view


urlpatterns = [
    path('', regiter_view, name='register_view'),

]