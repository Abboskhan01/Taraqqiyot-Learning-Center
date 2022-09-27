from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    phone_number = models.SmallIntegerField()
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    course_type = models.CharField(max_length=200)


