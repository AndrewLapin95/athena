from django.contrib import admin
from .models import UserProfile, Employee, BankInformation

# Register your models here.
admin.site.register(Employee)
admin.site.register(UserProfile)
admin.site.register(BankInformation)
