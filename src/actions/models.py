from django.db import models

# Create your models here.
class Action(models.Model):
    name = models.CharField(max_length=120)