from django.db import models

# Create your models here.
class accidental(models.Model):
    apartmentno =  models.ForeignKey('Apartments.Apartments',related_name='FlatName+',null=True,blank=True,on_delete=models.CASCADE)
    maintenanceid = models.ForeignKey('Maintenances.Maintenances',related_name='Apartmentsid+',null=True,blank=True,on_delete=models.CASCADE)
    maintenancedate = models.DateField()
