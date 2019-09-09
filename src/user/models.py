from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL

USER_TYPES = (
    ("EMPLOYEE", "employee"),
    ("MANAGER", "manager")
)

JOB_TITLES = (
    ("Back-End Developer", "BACKEND"),
    ("Front-End Developer", "FRONTEND"),
    ("DevOps Engineer", "DEVOPS"),
    ("UX Designer", "UX"),
    ("Intern", "INTERN")
)

TEAMS = (
    ("UI/UX Design Team", "UX_TEAM"),
    ("Backend Architecture", "BACKEND_TEAM"),
    ("Front-End Development Team", "FRONTEND_TEAM"),
    ("DevOps", "DEVOPS_TEAM"),
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
    role = models.CharField(max_length=20, choices=USER_TYPES)
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
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    job_title = models.CharField(max_length=20, choices=JOB_TITLES)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    team = models.CharField(max_length=20, choices=TEAMS)
    date_of_join = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=360, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    bank_information = models.OneToOneField(BankInformation, on_delete=models.CASCADE)
    profile_image_url = models.CharField(max_length=360, null=True, blank=True)

class EmergencyContact(models.Model):
    """
    Emergency contacts for a given employee
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    relationship = models.CharField(max_length=120, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)

class EducationInformation(models.Model):
    """
    Educational information of the employee
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class ExperienceInformation(models.Model):
    """
    Experience information of the employee
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Salary(models.Model):
    """
    Salary information for an employee
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField(null=True, blank=True)

class Department(models.Model):
    """
    Department information
    """
    name = models.CharField(max_length=120, null=True, blank=True)

class Designation(models.Model):
    """
    Designation information
    """
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)

class Vacation(models.Model):
    """
    Vacation information
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
