from django.db import models

# Create your models here.

class building(models.Model):
    buildingname = models.CharField(max_length=100)
    address = models.TextField()
    CITIES = (

        ('hubli', 'HUBLI'),
        ('dharwad', 'DHARWAD'),
        ('karwar', 'KARWAR'),
        ('gadag','GADAG'),
        ('haveri','HAVERI')
    )
    cities = models.CharField(max_length=10, choices=CITIES, default='True')

    STATE = (

        ('karanantak', 'KARANANTAK'),
        ('tamilnadu', 'TAMILNADU'),
        ('andrapradesh', 'ANDRAPRADESH'),
        ('DEHLI', 'DEHLI'),
        ('mumbai', 'MUMBAI')
    )
    state = models.CharField(max_length=10, choices= STATE, default='True')

    zip = models.IntegerField()

    landloardid = models.IntegerField(primary_key=True)