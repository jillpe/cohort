from django.db import models
import django_filters
from .models import JobTitle 


class JobTitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    tags__name = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter(lookup_expr='gte')

    class Meta: 
        model = JobTitle
        fields = ['company','name','tags__name', 'salary']
        