from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TAGS = (
    ("Job is Cool", "Job is Cool"),
    ("Job is Aight", "Job is Aight"),
    ("Technical Interview...thats tuff", "Technical Interview...thats tuff"),
    ("&#128175;", "&#128175;"),
)


class JobTitle(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    company = models.CharField(max_length=300)
    skills = models.TextField()
    initial_description = models.TextField()
    experience = models.IntegerField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True)
    tag = models.CharField(
        max_length=200,
        choices=TAGS,
        default=TAGS[0][0]
    )

    # this is kevins edit







    # this is kevins edit
