from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL

USER_TYPES = (
    (1, "employee"),
    (2, "manager")
)

JOB_TITLES = (
    ("Back-End Developer", "BACKEND"),
    ("Front-End Developer", "FRONTEND"),
    ("DevOps Engineer", "DEVOPS"),
    ("UX Designer", "UX"),
    ("Intern", "INTERN")
)

GENDER = (
    ("Femail", "FEMAIL"),
    ("Male", "MALE"),
    ("Other", "OTHER"),
)

# Create your models here.

class UserProfile(models.Model):
    """
    User profile class. Adds role and company role to the user field
    """
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(default=1, choices=USER_TYPES)
    company_alias = models.CharField(max_length=10, null=False, blank=False)

class BankInformation(models.Model):
    """
    Banking information class
    """
    owner = models.OneToOneField(USER, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=120, null=True, blank=True)
    bank_account_number = models.CharField(max_length=120, null=True, blank=True)
    swift_code = models.CharField(max_length=120, null=True, blank=True)

class Employee(models.Model):
    """
    Employee model class
    """
    owner = models.OneToOneField(USER, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    job_title = models.CharField(max_length=20, choices=JOB_TITLES)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    date_of_join = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    bank_information = models.OneToOneField(BankInformation, on_delete=models.CASCADE)
    