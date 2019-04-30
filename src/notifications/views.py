from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notification
# Create your views here.

class NotificationsListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = Notification.objects.none()

        return queryset