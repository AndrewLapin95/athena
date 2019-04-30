from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

EMPLOYEE = "EM"
MANAGER = "HR"

ROLE_CHOICES = (
    (EMPLOYEE, 'Employee'),
    (MANAGER, 'Manager'),
)

class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    role            = models.CharField(default=EMPLOYEE, max_length=2, choices=ROLE_CHOICES)
    company_alias   = models.CharField(max_length=10, null=False, blank=False)

# Create your models here.
class Employee(models.Model):
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=120)
    last_name       = models.CharField(max_length=120, null=True, blank=True)
    birthday        = models.DateField(null=True, blank=True)
    phone_number    = models.CharField(max_length=120, null=True, blank=True)
    address         = models.CharField(max_length=120, null=True, blank=True)