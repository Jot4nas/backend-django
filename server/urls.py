"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers 
from account.API import viewsets as accountviewsets 
<<<<<<< Updated upstream


=======
from account.API.viewsets import LoginView

>>>>>>> Stashed changes
# Configurando o DefaultRouter para rotas automáticas
route = routers.DefaultRouter()
route.register(r'accounts', accountviewsets.RegisterViewSet, basename="register")

# Definindo as rotas principais
urlpatterns = [
    # Rota do admin
    # Rota do admin
    path('admin/', admin.site.urls),
<<<<<<< Updated upstream
=======
    
    # Rota personalizada para login
    path('login/', accountviewsets.LoginView.as_view(), name='login'),

>>>>>>> Stashed changes
    # Incluindo as rotas do router
    path('', include(route.urls)),  
    
]
