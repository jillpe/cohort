from django.forms import ModelForm
from .models import Comment, JobTitle

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class JobTitleForm(ModelForm):
    class Meta:
        model = JobTitle
        fields = ['name','link','company','skills','initial_description','experience','location','salary']
