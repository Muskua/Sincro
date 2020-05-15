from django.urls import path
from . import views

urlpatterns = [
	path('', views.home), ## da sincro 'path('catalogo/', include('catalogo.urls')),' vogliamo riportare la views.home
]
