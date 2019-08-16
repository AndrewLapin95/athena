from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL

USER_TYPES = (
    (1, "employee"),
    (2, "manager")
)

class UserProfile(models.Model):
    """
    User profile class. Adds role and company role to the user field
    """
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(default=1, choices=USER_TYPES)
    company_alias = models.CharField(max_length=10, null=False, blank=False)

# Create your models here.
class Employee(models.Model):
    """
    Employee model class
    """
    owner = models.ForeignKey(USER, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    team = models.CharField(max_length=120, null=True, blank=True)
    date_of_joining = models.DateField()
    email = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=120, null=True, blank=True)
    manager = models.CharField(max_length=120, null=True, blank=True)

class EmergencyContact(models.Model):
    """
    Emergency contact model class
    """
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    relationship = models.CharField(max_length=120)
    birthday = models.DateField(null=False, blank=False)
    phone_number = models.CharField(max_length=120, null=False, blank=False)
    