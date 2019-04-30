from django.contrib import admin
# Register your models here.
from .models import UserProfile, Employee

admin.site.register(Employee)
admin.site.register(UserProfile)