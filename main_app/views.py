from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from .models import Comment, JobTitle
from .forms import CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def jobtitles_index(request):
  jobtitles = JobTitle.objects.all()
  return render(request, 'jobtitles/index.html', { 'jobtitles': jobtitles })

def jobtitles_detail(request, jobtitle_id):
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  comment_form = CommentForm()
  return render(request, 'jobtitles/detail.html', { 
    'jobtitle': jobtitle,
    'comment_form': comment_form 
  })

@login_required
def add_comment(request, jobtitle_id):
  form = CommentForm(request.POST)
  if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.jobtitle_id = jobtitle_id
      new_comment.save()
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def delete_comment(request, jobtitle_id, comment_id):
    jobtitle = JobTitle.objects.get(id=jobtitle_id)
    comment = Comment.objects.get(jobtitle_id=jobtitle_id, id=comment_id)
    jobtitle.comment_set.remove(comment)
    return redirect('detail', jobtitle_id=jobtitle_id)

def update_comment(request, jobtitle_id, comment_id):
    jobtitle = JobTitle.objects.get(id=jobtitle_id)
    comment = Comment.objects.get(id=comment_id)
    jobtitle.comment_set.remove(comment)
    comment_form = CommentForm(initial=model_to_dict(comment))
    return render(request, 'jobtitles/detail.html', { 
    'jobtitle': jobtitle,
    'comment_id': comment_id,
    'comment_form': comment_form 
  })

      
        # return redirect('detail', jobtitle_id=jobtitle_id)


class JobTitleCreate(CreateView):
  model = JobTitle
  fields = ['name', 'link', 'company', 'skills', 'initial_description', 'experience', 'location', 'salary']
  success_url = '/jobtitles/'

class JobTitleUpdate(UpdateView):
  model = JobTitle
  fields = '__all__'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

 
