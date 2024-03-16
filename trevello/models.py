from django.db import models


# Create your models here.

class Destination(models.Model):
    desc = models.CharField(max_length=200)
    name = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField()
