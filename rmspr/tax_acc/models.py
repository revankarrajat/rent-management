from django.db import models

# Create your models here.
class tax_acc(models.Model):
    id = models.AutoField(primary_key=True)
    tax_of_month = models.DateField()
    tax_of_year = models.DateField()
    tax_amt = models.DecimalField(max_digits=10,decimal_places=2)
    tax_paid_date = models.DateField()