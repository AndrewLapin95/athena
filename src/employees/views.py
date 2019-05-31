from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def employees_listview(request):
    template_name = "employees_list.html"
    context = {}
    return render(request, template_name, context)

def departments_listview(request):
    template_name = "departments_list.html"
    context = {}
    return render(request, template_name, context)

def designations_listview(request):
    template_name = "designations_list.html"
    context = {}
    return render(request, template_name, context)