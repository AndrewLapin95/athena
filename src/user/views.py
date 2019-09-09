import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, RedirectView, UpdateView, DeleteView, CreateView, ListView
from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, redirect, render

from .models import Employee, EmergencyContact, Salary, Department, Designation
from .forms import EmployeeUpdateForm, EmergencyContactCreateForm

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

class EmergencyContactDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete emergency contact
    """
    form_class = EmergencyContact
    template_name = "user/emergencycontact_confirm_delete.html"
    success_url = "/"
    
    def get_object(self, queryset=None):
        return get_object_or_404(EmergencyContact, id=self.kwargs.get("contact"))

class EmergencyContactCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new emergency contact
    """
    form_class = EmergencyContactCreateForm
    template_name = 'user/emergencycontact_create.html'
    success_url = "/"

    def form_valid(self, form):
        form.instance.employee = Employee.objects.filter(owner=self.request.user)[:1].get()
        return super(EmergencyContactCreateView, self).form_valid(form)

class SalaryListView(LoginRequiredMixin, ListView):
    """
    Provides a list of holidays
    """
    login_url = "/login/"
    template_name = "user/salary_list.html"

    def get_queryset(self):
        return Salary.objects.all()

class EmployeeListView(LoginRequiredMixin, ListView):
    """
    Provides a list of employees
    """
    login_url = "/login/"
    template_name = "user/employees_list.html"

    def get_queryset(self):
        return Employee.objects.all()

class DepartmentListView(LoginRequiredMixin, ListView):
    """
    Provides a list of departments
    """
    login_url = "/login/"
    template_name = "user/departments_list.html"

    def get_queryset(self):
        return Department.objects.all()

class DesignationListView(LoginRequiredMixin, ListView):
    """
    Provides a list of designations
    """
    login_url = "/login/"
    template_name = "user/designations_list.html"

    def get_queryset(self):
        return Designation.objects.all()


def vacation_listview(request):
    template_name = "user/vacation_list.html"
    context = {}
    return render(request, template_name, context)
