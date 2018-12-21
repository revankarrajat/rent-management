from django.db import models

# Create your models here.
class termination(models.Model):
    terminationid = models.PositiveIntegerField(primary_key=True)
    leavingdate = models.DateField()
    leavingreason = models.TextField()