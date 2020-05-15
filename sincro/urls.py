"""sincro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from custom_homepage.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls')),
    path('login/', include('login.urls')),
    path('private/', include('private.urls')),
    path('riepilogo/', include('riepilogo.urls')),
    path('', include('custom_homepage.urls')),
    path('incarico', include('incarico.urls')),
    path('polizza', include('polizza.urls')),
    path('computo', include('computo.urls')),
    path('relazione', include('relazione.urls')),
    path('videoperizia', include('videoperizia.urls')),
    path('allegati', include('allegati.urls')),
    path('partite', include('partite.urls')),
    path('garanzie', include('garanzie.urls')),

]
