from .models import (
    Doctor,
    Location,
    Contact,
    Practice
)
import django_filters
from account.models import Account

class DoctorFilter(django_filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ['user', 'description']