from django.db import models
from django.db.models.enums import Choices
import django_filters
from .models import JobTitle 
from django.db import models

class JobTitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    # tags = Tag.objects.values_list('id', 'name')
    tags__name = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter(lookup_expr='gte')

    class Meta: 
        model = JobTitle
        fields = ['company','name','tags__name', 'salary']

         