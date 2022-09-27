from django.shortcuts import render
from django.http import HttpResponse
from .models import Students


def regiter_view(request):
    if request.POST:
        model = Students()
        model.first_name = request.POST.get('first_name')
        model.last_name = request.POST.get('last_name')
        model.age = request.POST.get('age')
        model.phone_number = request.POST.get('phone_number')
        model.address = request.POST.get('address', 'Manzil kiritilmagan')
        model.email = request.POST.get('email', 'Email kiritilmagan')
        model.course_type = request.POST.get('course_type')
        model.save()
    return render(request, 'register.html')




