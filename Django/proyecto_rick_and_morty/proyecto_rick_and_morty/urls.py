"""proyecto_rick_and_morty URL Configuration

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
from django.urls import path
from proyecto_rick_and_morty.views import index, characters, planets, chapters
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('characters/', characters, name='characters'), # 'name' permite que HTML enlace la vista
    path('planets/', planets, name='planets'), 
    path('chapters/', chapters, name='chapters'), 
]
