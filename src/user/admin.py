from django.contrib import admin
from .models import UserProfile, Employee, BankInformation, EmergencyContact, EducationInformation, ExperienceInformation, Salary, Department, Designation

# Register your models here.
admin.site.register(Employee)
admin.site.register(UserProfile)
admin.site.register(BankInformation)
admin.site.register(EmergencyContact)
admin.site.register(EducationInformation)
admin.site.register(ExperienceInformation)
admin.site.register(Salary)
admin.site.register(Department)
admin.site.register(Designation)
