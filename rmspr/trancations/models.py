from django.db import models

# Create your models here.


class trancations(models.Model):
    paymentid = models.AutoField(primary_key=True)
    paymentdate = models.DateField()
    paymentamount = models.DecimalField(max_digits=10,decimal_places=2)

    PAYMENT = (
        ('cash', 'CASH'),
        ('check', 'CHECK'),
        ('creditcard', 'CREDITCARD'),
    )
    paymentmethod = models.CharField(max_length=10,choices=PAYMENT,default='True')



class checkpayment(models.Model):
        bankname = models.CharField(max_length=100,primary_key=True)
        accno = models.IntegerField()
        amount = models.DecimalField(max_digits=10,decimal_places=2)


class  creditcard(models.Model):

        bankname = models.ForeignKey('trancations.checkpayment', related_name="bankname+", null=True, blank=True,on_delete=models.CASCADE)
        holdername = models.CharField(max_length=100)
        accountype = models.CharField(max_length=100)
        accno = models.ForeignKey('trancations.checkpayment', related_name="accno+", null=True, blank=True,on_delete=models.CASCADE)
        expdate = models.IntegerField()



