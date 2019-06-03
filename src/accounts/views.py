from django.shortcuts import render

# Create your views here.
def payments_listview(request):
    template_name = "payments_list.html"
    context = {}
    return render(request, template_name, context)

def expenses_listview(request):
    template_name = "expenses_list.html"
    context = {}
    return render(request, template_name, context)

def taxes_listview(request):
    template_name = "taxes_list.html"
    context = {}
    return render(request, template_name, context)