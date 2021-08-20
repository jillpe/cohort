from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tags_detail", kwargs={"pk": self.id})
    

class JobTitle(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    company = models.CharField(max_length=300)
    skills = models.TextField()
    initial_description = models.TextField()
    experience = models.IntegerField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joblist = models.ManyToManyField(JobTitle)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True)
