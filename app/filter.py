import django_filters
from .models import formregistration

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = formregistration
        fields = [
            'wage',
            'gender',
            'job',
            'jobtype',
            'location',



        ]

class PersonFilters(django_filters.FilterSet):
    class Meta:
        model = formregistration
        fields = [
            'wage',
            'job',

        ]
