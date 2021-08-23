import django_filters
from .models import JobTitle



class JobTitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # what does this do 
    class Meta: 
        model = JobTitle
        fields = ['company','name']
         