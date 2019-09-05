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
from user.views import EmployeeDetailView, EmployeeUpdateView, ProfileRedirectView
from employees.views import employees_listview, departments_listview, designations_listview
from accounts.views import expenses_listview, payments_listview
from salary.views import salary_listview
from jobs.views import jobs_listview, candidates_listview
from vacations.views import  holidays_listview, vacation_listview
from settings.views import settings_listview
from settings.views import password_listview

from django.contrib import admin
from django.urls import re_path
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    re_path(r'^login', LoginView.as_view(), name='login'),
    re_path(r'^logout', LogoutView.as_view(), name='logout'),
    re_path(r'^profile/(?P<username>[\w-]+)', EmployeeDetailView.as_view(), name='home'),
    re_path(r'^update-profile', EmployeeUpdateView.as_view(), name='update-profile'),
    re_path(r'^employees', employees_listview, name='employees'),
    re_path(r'^holidays', holidays_listview, name='holidays'),
    re_path(r'^vacation', vacation_listview, name='vacation'),
    re_path(r'^departments', departments_listview, name='departments'),
    re_path(r'^designations', designations_listview, name='designations'),
    re_path(r'^expenses', expenses_listview, name='expenses'),
    re_path(r'^payments', payments_listview, name='payments'),
    re_path(r'^salary', salary_listview, name='salary'),
    re_path(r'^jobs', jobs_listview, name='jobs'),
    re_path(r'^candidates', candidates_listview, name='candidates'),
    re_path(r'^settings', settings_listview, name='settings'),
    re_path(r'^password', password_listview, name='password'),
    re_path(r'^admin', admin.site.urls, name='admin'),
    re_path(r'^', ProfileRedirectView.as_view(), name='redirect'),
]
