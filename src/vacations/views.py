from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Holiday
from .forms import HolidayCreateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView

# Create your views here.
class HolidayListView(LoginRequiredMixin, ListView):
    """
    Provides a list of holidays
    """
    login_url = "/login/"
    template_name = "vacations/holidays_list.html"

    def get_queryset(self):
        return Holiday.objects.all()

class HolidayCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new holiday
    """
    form_class = HolidayCreateForm
    template_name = "vacations/holidaycreate_form.html"
    success_url = "/holidays"

class HolidayDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a holiday
    """
    form_class = Holiday
    template_name = "vacations/holidaydelete_form.html"
    success_url = "/holidays"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Holiday, id=self.kwargs.get("holiday"))

def vacation_listview(request):
    template_name = "vacations/vacation_list.html"
    context = {}
    return render(request, template_name, context)