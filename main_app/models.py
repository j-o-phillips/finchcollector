from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    territory = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    color = models.CharField( max_length=100)
