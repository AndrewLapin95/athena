import logging


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, RedirectView, UpdateView
from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, redirect

from .models import Employee
from .forms import EmployeeUpdateForm

# Create your views here.

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """
    Lists employees for a given user
    """
    login_url = "/login/"

    def get_object(self):
        username = self.request.user

        if username is None or str(username) != self.kwargs.get("username"):
            raise Http404

        return get_object_or_404(Employee, owner=username)

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update employee's personal imformation
    """
    form_class = EmployeeUpdateForm
    template_name = "user/profile_info.html"
    success_url = "/"

    def get_object(self):
        username = self.request.user
        return get_object_or_404(Employee, owner=username)

class ProfileRedirectView(RedirectView):
    """
    Redirect to the main profile page for the user
    """
    permanent = False

    def get_redirect_url(self, *args, **kwards):  
        username = self.request.user

        if username is None:
            raise Http404

        return "profile/{}".format(username)
