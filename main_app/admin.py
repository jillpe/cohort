from django.contrib import admin
from .models import JobTitle, Applicant, Comment, Tag

admin.site.register(JobTitle)
admin.site.register(Applicant)
admin.site.register(Comment)
admin.site.register(Tag)
