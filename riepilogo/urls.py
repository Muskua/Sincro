from django.urls import path
from . import views

urlpatterns = [
	## dobbiamo creare una def home(): all'interno di views.py quindi
	path('', views.home), ## da sincro 'path('catalogo/', include('catalogo.urls')),' vogliamo riportare la views.home
]