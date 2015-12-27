from django.shortcuts import render, redirect, get_object_or_404
from .models import Spot
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import *

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# Create your views here.

def index(request):
	return render(request, 'main/bside.html')
def start(request):
	return render(request, 'main/start.html')
def find(request):
	spotlist = Spot.objects.all().order_by('-id')	
	return render(request, 'main/find.html', { 'spotlist' : spotlist })
def about(request):
	return render(request, 'main/about.html')
def end(request):
	spotlist = Spot.objects.all().order_by('-id')	
	return render(request, 'main/end.html', { 'spotlist' : spotlist })

def startsesh(request):
	if request.method == 'POST':
		if request.POST['time']:
			fix = 0
			lat = float(request.POST['lat'])
			lon = float(request.POST['lon'])

			if is_number(request.POST['time']):
			# 	sesh = Spot(name = request.POST['name'], description = request.POST['description'], lat = lat, lon = lon, time = request.POST['time'], made = timezone.now())
			# else:
				fix = int(request.POST['time'])
				sesh = Spot(name = request.POST['name'], description = request.POST['description'], lat = lat, lon = lon, time = fix, made = timezone.now())
				sesh.save()
			else:
				messages.error(request, 'ENTER NUMBER')
				return HttpResponseRedirect(reverse('main:start'))
		return HttpResponseRedirect(reverse('main:find'))
	else:
		return HttpResponseRedirect(reverse('main:index'))

def delete(request, spot_id):
	vic = get_object_or_404(Spot, id = spot_id)
	vic.delete()
	return HttpResponseRedirect(reverse('main:end'))
