from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.

def user_listview(request):
    template_name = "user/user.html"
    queryset = User.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)