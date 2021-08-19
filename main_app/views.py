from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Finch, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return HttpResponse(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', { 'finches': finches })

@login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have 
    })

@login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ['wingspan', 'description', 'age']

class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Cat.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

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
