from django.db import models
from django.utils import timezone

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
		return (self.made) - now
	def __unicode__(self):
		return self.name