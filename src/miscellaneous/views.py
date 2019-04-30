from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Misc
# Create your views here.

class MiscellaneousListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = Misc.objects.none()

        return queryset