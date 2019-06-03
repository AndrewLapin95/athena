from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def holidays_listview(request):
    template_name = "holidays_list.html"
    context = {}
    return render(request, template_name, context)

def vacation_listview(request):
    template_name = "vacation_list.html"
    context = {}
    return render(request, template_name, context)