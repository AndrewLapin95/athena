from django.shortcuts import render

# Create your views here.

def notifications_listview(request):
    template_name = "notifications/notifications.html"
    context = {}
    return render(request, template_name, context)