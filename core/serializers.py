from rest_framework import serializers
from django.contrib.auth.models import Group

from account.models import Account as User
from .models import (
    Doctor
)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor