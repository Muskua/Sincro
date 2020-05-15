from django.shortcuts import render, HttpResponse

# Create your views here.

## When we call views.home in our app urls.py, we call this def through request
def home(request):

	## potremmo utilizzare render, per trasferire la visualizzazione del file login.html in questo caso, creiamolo
	return render(request, 'partite/partite.html')