from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TAGS = (
    ('1', 'Job is Cool'),
    ('2', 'Job is Aight'),
    ('3', 'Technical Interview...thats tuff'),
    ('4', '&#128175;'),
    ('5', '')
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
        max_length=1,
        choices=TAGS,
        default=TAGS[0][0]
    )

    







