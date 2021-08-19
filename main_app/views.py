from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JobTitle

# Create your views here.
def home(request):
    return render(request, 'home.html')

def jobtitles_index(request):
  jobtitles = JobTitle.objects.all()
  return render(request, 'jobtitles/index.html', { 'jobtitles': jobtitles })

def jobtitles_detail(request, jobtitle_id):
  jobtitle = JobTitle.objects.get(id=jobtitle_id)
  return render(request, 'jobtitles/detail.html', { 'jobtitle': jobtitle })

class JobTitleCreate(CreateView):
  model = JobTitle
  fields = '__all__'
  success_url = '/jobtitles/'

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
