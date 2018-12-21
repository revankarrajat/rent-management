from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = PhoneNumberField()
    password = models.CharField(max_length=100)

