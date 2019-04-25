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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

from user.views import EmployeeListView

from actions.views import actions_listview
from notifications.views import notifications_listview
from miscellaneous.views import misc_listview

urlpatterns = [

    re_path(r'^admin/', admin.site.urls, name="admin"),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^profile/', EmployeeListView.as_view(), name='home'),
    re_path(r'^actions/', actions_listview, name="actions"),
    re_path(r'^notifications/', notifications_listview, name="notifications"),
    re_path(r'misc/', misc_listview, name="misc"),
    re_path(r'', RedirectView.as_view(url='/profile/', permanent=True)),
]
