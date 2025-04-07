from django_filters import FilterSet
from .models import Course


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'level': ['exact'],
            'price': ['gt', 'lt'],
            'created_by': ['exact']

        }

