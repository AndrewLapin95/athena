from django.shortcuts import render

# Create your views here.

def misc_listview(request):
    template_name = "miscellaneous/miscellaneous.html"
    context = {}
    return render(request, template_name, context)