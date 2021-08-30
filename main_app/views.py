from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from .models import User, Comment, JobTitle, Tag, Applicant
from .forms import CommentForm, JobTitleForm, TagForm, PersonalInfoForm
from .filter import JobTitleFilter

def home(request):
    job_title_form = JobTitleForm()
    return render(request, 'home.html', {'job_title_form': job_title_form })

def jobtitles_index(request):
  jobtitles = JobTitle.objects.all()
  job_title_form = JobTitleForm()
  myFilter = JobTitleFilter(request.GET, queryset=jobtitles)
  jobtitles = myFilter.qs
  return render(request, 'jobtitles/index.html', { 'jobtitles': jobtitles, 'myFilter': myFilter, 'job_title_form': job_title_form })

def jobtitles_detail(request, jobtitle_id):
  job_title_form = JobTitleForm()
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  tags_jobtitle_doesnt_have = Tag.objects.exclude(id__in = jobtitle.tags.all().values_list('id'))
  tag_form = TagForm()
  comment_form = CommentForm()
  return render(request, 'jobtitles/detail.html', { 
    'jobtitle': jobtitle,
    'comment_form': comment_form,
    'tags': tags_jobtitle_doesnt_have,
    'job_title_form':job_title_form,
    'tag_form':tag_form
  })

@login_required
def create_new_job(request):
  form = JobTitleForm(request.POST)
  if form.is_valid():
    new_job = form.save(commit=False)
    new_job.save()
  return redirect('index')

@login_required
def add_comment(request, jobtitle_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.jobtitle_id = jobtitle_id
    new_comment.user = User.objects.get(id=request.user.id)
    new_comment.save()
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def delete_comment(request, jobtitle_id, comment_id):
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  comment = Comment.objects.get(jobtitle_id=jobtitle_id, id=comment_id)
  if request.user.id == comment.user.id:
    jobtitle.comment_set.remove(comment)
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def update_comment(request, jobtitle_id, comment_id):
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  comment = Comment.objects.get(id=comment_id)
  comment_form = CommentForm(initial=model_to_dict(comment))
  if request.user.id == comment.user.id:
    jobtitle.comment_set.remove(comment)
    job_title_form = JobTitleForm()
    return render(request, 'jobtitles/detail.html', { 
    'jobtitle': jobtitle,
    'comment_id': comment_id,
    'comment_form': comment_form,
    'job_title_form': job_title_form
  })
  else:
    return redirect('detail', jobtitle_id=jobtitle_id)

class JobTitleCreate(LoginRequiredMixin, CreateView):
  model = JobTitle
  fields = ['name', 'link', 'company', 'skills', 'initial_description', 'experience', 'location', 'salary']
  success_url = '/jobtitles/'


class JobTitleUpdate(LoginRequiredMixin, UpdateView):
  model = JobTitle
  fields = '__all__'

class TagList(LoginRequiredMixin, ListView):
  model = Tag

class TagCreate(LoginRequiredMixin, CreateView):
  model = Tag
  fields = ['name']

class TagUpdate(LoginRequiredMixin, UpdateView):
  model = Tag
  fields = ['name']

class TagDelete(LoginRequiredMixin, DeleteView):
  model = Tag
  success_url = '/tags/'

@login_required
def create_new_tag(request):
  form = TagForm(request.POST)
  if form.is_valid():
    new_tag = form.save()
    new_tag.user.set([request.user]);
  return redirect('index')

@login_required
def assoc_tag(request, jobtitle_id, tag_id):
  JobTitle.objects.get(id=jobtitle_id).tags.add(tag_id)
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def unassoc_tag(request, jobtitle_id, tag_id):
  tag = Tag.objects.get(id=tag_id)
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  tag.jobtitle_set.remove(jobtitle)
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def applicants_detail(request, applicant_id):
  applicant = Applicant.objects.get(id=applicant_id)
  personal_info_form = PersonalInfoForm(initial=model_to_dict(applicant))
  job_title_form = JobTitleForm()
  return render(request, 'applicants/detail.html', {'applicant':applicant, 'job_title_form': job_title_form, 'personal_info_form': personal_info_form})

@login_required
def assoc_job(request, jobtitle_id):
  user = User.objects.get(id=request.user.id)
  user.applicant.joblist.add(jobtitle_id)
  user.save()
  return redirect('index')

@login_required
def unassoc_job(request, jobtitle_id, applicant_id):
  user = User.objects.get(id=request.user.id)
  user.applicant.joblist.remove(jobtitle_id)
  user.save()
  applicant = Applicant.objects.get(id=applicant_id)
  return redirect('applicants_detail', applicant_id = applicant_id )

@login_required
def assoc_user(request, jobtitle_id):
  user_id = User.objects.get(id=request.user.id)
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  jobtitle.user.add(user_id)
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def unassoc_user(request, jobtitle_id):
  user_id = User.objects.get(id=request.user.id)
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  jobtitle.user.remove(user_id)
  return redirect('detail', jobtitle_id=jobtitle_id)

@login_required
def applicants_change_privacy(request, applicant_id):
  applicant = Applicant.objects.get(id=applicant_id)
  user = User.objects.get(id=request.user.id)
  if user.applicant.id == applicant.id:
    applicant.is_public = not applicant.is_public
    applicant.save()
  return redirect('applicants_detail', applicant_id=applicant_id)

def applicants_add_info(request, applicant_id):
  form = PersonalInfoForm(request.POST, instance=Applicant.objects.get(id=applicant_id))
  if form.is_valid():
    form.save()
  return redirect('applicants_detail', applicant_id=applicant_id)
  


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