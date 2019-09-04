from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
def settings_listview(request):
    template_name = "settings_list.html"
    context = {}
    return render(request, template_name, context)

def password_listview(request):
    template_name = "password_list.html"
    context = {}
    return render(request, template_name, context)