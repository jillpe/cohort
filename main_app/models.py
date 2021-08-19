from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class JobTitle(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    company = models.CharField(max_length=300)
    skills = models.TextField()
    initial_description = models.TextField()
    experience = models.IntegerField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=500)

    def __str__(self):
        return self.name


