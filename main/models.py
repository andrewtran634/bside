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
		skate = (self.made) + timedelta(hours = self.time)
		timeleft = skate - now

		if (timeleft.total_seconds() <= 0):
			return 0;
		else:
			return (timeleft.total_seconds()/3600.0)

	def __unicode__(self):
		return self.name
