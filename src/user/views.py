from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.urls import reverse

from .models import Employee

# Create your views here.

class EmployeeListView(LoginRequiredMixin, ListView):

    login_url = "/login/"

    def get_queryset(self):
        queryset = Employee.objects.none()
        try:
            owner = User.objects.get(username=self.request.user).id
            user_id = Employee.objects.get(owner_id=owner).id
        except:
            return queryset

        if user_id is not None:
            queryset = Employee.objects.filter(
                Q(id=user_id)
            )

        return queryset