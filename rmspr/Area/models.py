from django.db import models
import math

# Create your models here.
class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    shop_office_no = models.PositiveIntegerField()
    length_in_ft = models.PositiveIntegerField()
    width_in_ft = models.PositiveIntegerField()
    total_area = models.PositiveIntegerField
    rent_per_sqft = models.PositiveIntegerField()
    total_rent = models.PositiveIntegerField()







