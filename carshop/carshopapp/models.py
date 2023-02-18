from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=255, default = "Car")
    color = models.CharField(max_length=255, default = "White")
    power = models.IntegerField(default = 1)
    price = models.IntegerField(default = 2)
    max_speed = models.IntegerField(default = 3)
    fuel_consumption = models.IntegerField(default = None, blank=True, null=True)
    overclocking = models.IntegerField(default = 5)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, default = "6")

class Description(models.Model):
    author = models.CharField(max_length=255, default = "User")
    description = models.TextField()
