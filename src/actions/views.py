from django.shortcuts import render

# Create your views here.

def actions_listview(request):
    template_name = "actions/actions.html"
    context = {}
    return render(request, template_name, context)