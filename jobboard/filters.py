import django_filters


from .models import *

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = PostJob
        fields = ('location','salary','type_job')