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
from dj_rest_auth.views import LoginView, LogoutView
from profileAuth.API.viewsets import CustomRegisterView  # Importando a view personalizada

urlpatterns = [
    # Rota do admin
    path('admin/', admin.site.urls),
    
    # URLs de login e logout do dj_rest_auth
    path('api/auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),
    
    # URL de registro utilizando a sua view personalizada
    path('api/auth/registration/', CustomRegisterView.as_view(), name='rest_register'),
   
    # Incluindo as URLs do dj_rest_auth para o gerenciamento de usuários e autenticação
    path('api/auth/', include('dj_rest_auth.urls')),
    
    # Incluindo as URLs do allauth (se necessário, como para login via redes sociais)
    path('api/auth/social/', include('allauth.socialaccount.urls')),
]
