from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request, 'custom_homepage/homepage_view.html')