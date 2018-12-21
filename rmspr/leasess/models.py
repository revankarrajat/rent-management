from django.db import models

# Create your models here.
class leasess(models.Model):
    leasessid = models.IntegerField(primary_key=True)
    landlordname = models.CharField(max_length=100)
    tenantname = models.CharField(max_length=100)
    apartmentsname = models.CharField(max_length=100,blank=True, default=None)
    housename = models.CharField(max_length=100,blank=True, default=None)
    startdate = models.DateField()
    enddate = models.DateField()
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    securitydeposit = models.DecimalField(max_digits=10,decimal_places=2)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()

class renewal(models.Model):
    renewalid = models.IntegerField(primary_key=True)
    renewaldate = models.DateField()
    renewalperiod = models.CharField(max_length=100)
    leasessid= models.ForeignKey('leasess',related_name= 'leasessid+',null=True, default=None,on_delete=models.CASCADE)

