from django.db import models

# Create your models here.
class Spot(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	lon = models.FloatField()
	lat = models.FloatField()