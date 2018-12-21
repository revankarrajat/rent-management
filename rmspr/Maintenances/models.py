from django.db import models

# Create your models here.

class Maintenances(models.Model):
    Apartmentsid = models.IntegerField()
    Maintenances_of_month = models.DateTimeField()
    Maintenances_of_year = models.DateTimeField()
    Maintenances_amount = models.DecimalField(max_digits=10, decimal_places=2)
    Maintenances_paid_date = models.DateField()

