from django.db import models

# Create your models here.

class Holiday(models.Model):
    """
    Model representing a holiday
    """
    title = models.CharField(max_length=120, null=True, blank=True)
    holiday_date = models.DateField(null=True, blank=True)
    week_day = models.CharField(max_length=120, null=True, blank=True)
