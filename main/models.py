from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Spot(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	lon = models.FloatField()
	lat = models.FloatField()
	time = models.FloatField()
	made = models.DateTimeField('time')

	def timeleft(self):
		now = timezone.now()
		time = ((self.made.hour) + self.time - now.hour)#timedelta(hours = self.time) - now)
		return int(time)
	def __unicode__(self):
		return self.name