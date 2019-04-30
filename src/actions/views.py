from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Action
# Create your views here.

class ActionsListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = Action.objects.none()

        return queryset