from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def salary_listview(request):
    template_name = "salary_list.html"
    context = {}
    return render(request, template_name, context)