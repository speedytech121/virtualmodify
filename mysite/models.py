from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=10,default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
