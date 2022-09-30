from django.db import models

# Create your models here.
class Follower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)
    course_type = models.CharField(max_length=200)