from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def jobs_listview(request):
    template_name = "jobs_list.html"
    context = {}
    return render(request, template_name, context)

def candidates_listview(request):
    template_name = "salary_list.html"
    context = {}
    return render(request, template_name, context)