from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def activities_listview(request):
    template_name = "activities_list.html"
    context = {}
    return render(request, template_name, context)