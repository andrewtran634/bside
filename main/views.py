from django.shortcuts import render, redirect, get_object_or_404
from .models import Spot
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import timezone


# Create your views here.

def index(request):
	return render(request, 'main/bside.html')
def start(request):
	return render(request, 'main/start.html')
def find(request):
	spotlist = Spot.objects.all()	
	return render(request, 'main/find.html', { 'spotlist' : spotlist })
def about(request):
	return render(request, 'main/about.html')
def end(request):
	spotlist = Spot.objects.all()	
	return render(request, 'main/end.html', { 'spotlist' : spotlist })

def startsesh(request):
	if request.method == "POST":
		if request.POST['time']:
			lat = float(request.POST['lat'])
			lon = float(request.POST['lon'])
			if int(request.POST['time']):
				sesh = Spot(name = request.POST['name'], description = request.POST['description'], lat = lat, lon = lon, time = request.POST['time'], made = timezone.now())
			else:
				fix = int(request.Post['time'])
				sesh = Spot(name = request.POST['name'], description = request.POST['description'], lat = lat, lon = lon, time = fix, made = timezone.now())
		else:
			sesh = Spot(name = request.POST['name'], description = request.POST['description'], time = 2, made = timezone.now())		

		sesh.save()
		return HttpResponseRedirect(reverse('main:find'))
	else:
		return HttpResponseRedirect(reverse('main:index'))

def delete(request, spot_id):
	vic = get_object_or_404(Spot, id = spot_id)
	vic.delete()
	return HttpResponseRedirect(reverse('main:end'))
