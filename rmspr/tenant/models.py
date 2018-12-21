from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    tenant_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = PhoneNumberField()
    deposit_amount = models.PositiveIntegerField()
    gst_no = models.CharField(max_length=100,blank=True, default=None)
    acc_name = models.CharField(max_length=100)
    acc_no = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=100)
    bank_branch_name = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=100)
