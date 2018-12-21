from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        res = str(self.username)
        return res


class property(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(default='', blank=False)
    price = models.IntegerField(blank=False)
    location = models.CharField(max_length=50, blank=False, null=False)
    num_views = models.IntegerField(default=0)
    avg_rating = models.IntegerField(default=0)
    property_img = models.ImageField(null=True, blank=True, upload_to="property_img/")
    owner = models.ForeignKey('managment.owner', related_name='+', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    profile = models.TextField(blank=False)
    pref_location = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username;


class owner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    num_properties = models.IntegerField(default=0)
    owner_name = models.CharField(max_length=30)
    email = models.EmailField(default='')
    phone_no = PhoneNumberField(default='')
    def __str__(self):
        return self.owner_name


class review(models.Model):
    prop_id = models.ForeignKey('managment.property', related_name='id+', on_delete=models.CASCADE, null=True)
    visitor_id = models.ForeignKey('managment.visitor', related_name='id+', on_delete=models.CASCADE, null=True)

    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s %s %s" % (self.comment, self.rating, self.visitor_id)
