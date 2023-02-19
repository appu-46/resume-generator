from django.db import models
from django.utils import timezone

from .models import *
# Create your models here.


class Header(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=20)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Body(models.Model):
    header_models = models.ForeignKey(Header, on_delete=models.CASCADE)

    # class work_experience(models.Model):
    # no_of_companies_worked_in = models.IntegerField()
    company_name = models.CharField(max_length=20)
    position = models.CharField(max_length=15)
    time_period = models.CharField(max_length=15)
    responsibilites = models.CharField(max_length=200)

    # class projects(models.Model):
    project_title = models.CharField(max_length=20)
    project_description = models.CharField(max_length=50)

    # class achivements (models.Model):
    achievement_title = models.CharField(max_length=15)
    achievement_description = models.CharField(max_length=50)

    # class skills(models.Model):
    skills = models.CharField(max_length=15)
    pub_date = models.DateTimeField()
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.header_models
