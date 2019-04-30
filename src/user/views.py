import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.db.models import Q

from .models import Employee

# Create your views here.

class EmployeeListView(LoginRequiredMixin, ListView):
    """
    Lists employees for a given user
    """
    login_url = "/login/"

    def get_queryset(self):
        queryset = Employee.objects.none()
        try:
            owner = User.objects.get(username=self.request.user).id
            user_id = Employee.objects.get(owner_id=owner).id
        except Exception as e:
            logging.warning("Couldn't retreieve the employee set.")
            logging.warning("The error was: {}".format(str(e)))
            return queryset

        if user_id is not None:
            queryset = Employee.objects.filter(
                Q(id=user_id)
            )

        return queryset