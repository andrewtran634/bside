from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, 'main/bside.html')
def start(request):
	return render(request, 'main/start.html')
def find(request):
	return render(request, 'main/find.html')
def about(request):
	return render(request, 'main/about.html')
def end(request):
	return render(request, 'main/end.html')
def startsesh(request):
	if request.method == "POST":
		if request.POST['time']:
			if int(request.POST['time']):
				sesh = Spot(name = request.POST['name'], description = request.POST['description'], time = request.POST['time'])
			else:
				return redirect(reverse)
		else:
			sesh = Spot(name = request.POST['name'], description = request.POST['description'], time = 2)			
		sesh.save()
		redirect(reverse('main:find'))
	else:
		redirect(reverse('main:index'))

