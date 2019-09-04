from django.shortcuts import render, redirect

# Create your views here.
def payments_listview(request):
    template_name = "payments_list.html"
    context = {}

    if request.user.userprofile.role == "MANAGER":
        return render(request, template_name, context)
    else:
        return redirect("/")

def expenses_listview(request):
    template_name = "expenses_list.html"
    context = {}
    return render(request, template_name, context)