from django.db import models

# Create your models here.

class Apartments(models.Model):
    FlatName = models.CharField(max_length=100)
    Address = models.TextField()
    Descriptions = models.TextField()
    City = models.CharField(max_length=100)


