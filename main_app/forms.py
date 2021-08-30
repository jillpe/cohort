from django.db.models import fields
from django.forms import ModelForm

from .models import Comment, JobTitle, Tag


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class JobTitleForm(ModelForm):
    class Meta:
        model = JobTitle
        fields = ['name','link','company','skills','initial_description','experience','location','salary']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

