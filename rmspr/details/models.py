from django.db import models

# Create your models here.
class details(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Phone = models.BigIntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Name