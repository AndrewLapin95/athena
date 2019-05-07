"""Athena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from user.views import EmployeeListView
from documents.views import DocumentsTemplateView
from earnings.views import EarningsTemplateView
from personal.views import VacationTemplateView
from events.views import EventsTemplateView

from django.contrib import admin
from django.urls import re_path
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^documents/', DocumentsTemplateView.as_view(), name='documents'),
    re_path(r'^earnings/', EarningsTemplateView.as_view(), name='earnings'),
    re_path(r'^vacation/', VacationTemplateView.as_view(), name='vacation'),
    re_path(r'^events/', EventsTemplateView.as_view(), name='events'),
    re_path(r'^profile/', EmployeeListView.as_view(), name='home'),
    re_path(r'^admin/', admin.site.urls, name='admin'),
    re_path(r'^$', RedirectView.as_view(url='/profile/', permanent=False)),
]
