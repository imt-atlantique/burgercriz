"""burgercriz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import HomeView, UserUpdateView, help_view, apps_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', login_required(UserUpdateView.as_view()), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('apps/', apps_view, name='apps'),
    path('help/', help_view, name='help'),
    path('cards/', include('cards.urls')),
]
