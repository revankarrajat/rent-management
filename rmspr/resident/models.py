from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class resident(models.Model):
    id = models.AutoField(primary_key=True)
    res_firstname = models.CharField(max_length=100)
    res_lastname = models.CharField(max_length=100)
    res_email_id = models.EmailField()
    res_landline_no = PhoneNumberField()
    res_phone_no = PhoneNumberField()
    notes = models.TextField()
    attachment = models.FileField()
