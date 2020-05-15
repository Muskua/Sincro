from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('', LoginView.as_view(), {'template_name': 'login/login.html'}),
	#path('', views.home), ## da sincro 'path('catalogo/', include('catalogo.urls')),' vogliamo riportare la views.home
]