from django.db import models
import django_filters
from .models import JobTitle 

choices = (
    (0, '<$50,000'),
    (50000, '$50,000'),
    (75000, '$75,000'),
    (100000, '$100,000'),
    (125000, '$125,000'),
    (150000, '$150,000'),
    (175000, '$175,000'),
    (200000, '$200,000'),
    (225000, '$225,000'),
    (250000, '$250,000')
)


class JobTitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    tags__name = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.ChoiceFilter(choices = choices, lookup_expr='gte')
    #NumberFilter(lookup_expr='gte')

    class Meta: 
        model = JobTitle
        fields = ['company','name','tags__name', 'salary']
        