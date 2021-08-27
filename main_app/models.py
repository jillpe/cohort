from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tags_index")

class JobTitle(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    company = models.CharField(max_length=300)
    skills = models.CharField(max_length=1000, blank=True, null=True)
    initial_description = models.CharField(max_length=1000, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    user = models.ManyToManyField(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joblist = models.ManyToManyField(JobTitle)
    is_public = models.BooleanField(default=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    pronoun = models.CharField(max_length=50)
    about_me = models.TextField(max_length=500)
    state_location = models.CharField(max_length=100)
    city_location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_applicant(sender, instance, created, **kwargs):
    if created:
        Applicant.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_applicant(sender, instance, **kwargs):
    instance.applicant.save()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.comment)

    def get_absolute_url(self):
        return reverse("jobs_detail", kwargs={"pk": self.id})