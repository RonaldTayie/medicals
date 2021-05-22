
import json

import requests
from account.models import Account
from django.contrib.auth.models import Group
from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,
                                   HTTP_406_NOT_ACCEPTABLE,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView

# Filters
from .filter import *
from .models import City, Country, DoctorQualification, State

def acc_to_dict(account=None):
    account._mutable = False
    u = model_to_dict(account,exclude=['password','user_permissions','is_superuser','is_staff','last_login','groups'])
    if u.get('profile_img') != None:
        u['profile_img'] = account.profile_img.url
    u['date_joined'] = str(account.date_joined)
    return u

def request_filters(request):
    filters = {}
    for k,vals in request.GET.lists():
        for v in vals:
            filters[k] = v
    # return filters
    return filters


@api_view(['GET'])
def index(request):
    accounts = Account.objects.all()
    users = []
    for account in accounts:
        users.append(acc_to_dict(account))
    return Response(users)

# ======== Doctor =============

# Get / List Doctor
@api_view(['GET'])
def doctor(request):
    if not request.GET.get('user'):
        doctors_list = Doctor.objects.all()[0:10]
    else:
        doctors_list = Doctor.objects.filter(user__uid=request.GET.get('user'))
    doctors_records = DoctorFilter(request.GET, queryset=doctors_list)
    doctors = []
    for doctor in doctors_list:
        doctor._mutable = False
        doc = model_to_dict(doctor)
        doc['user'] = acc_to_dict(doctor.user)
        doctors.append(doc)
    
    return Response(doctors)

# Search doctor
@api_view(['GET'])
def search_doctor(request):
    # Start the search from the contacts
    all_contacts = Contact.objects.filter(isDoctor=True)
    req_filters = request_filters(request)
    doctor = Doctor.objects.all()
    doctors = []
    for doc in doctor.complex_filter(req_filters):
        doctors.append(model_to_dict(doc))
    
    return Response(doctors)

# Get a particular Doctor
@api_view(['GET'])
def get_doctor(request):
    doc_id = request.GET.get('id')
    doctor = Doctor.objects.get(id=doc_id)
    
    doctor._mutable = False
    doc = model_to_dict(doctor)
    doc['user'] = acc_to_dict(doctor.user)
    return Response(doc)

@api_view(['GET'])
def practice(request):
    all_practices = Practice.objects.all()
    return Response([])

@api_view(['GET'])
def search_prectice(request):
    # Filter for the search
    filters = request_filters(request)
    return Response(filters)

@api_view(['GET'])
def init_world(request):
    countries = requests.get('http://192.168.1.103/data/countries.json')

    data = json.loads(countries.content)
    for country in data:
        c = Country
        c.name = country["name"]
        c.phone_code = country['phone_code']
        c.iso2 = country['iso2']
        c.iso3 = country['iso3']
        c.capital = country['capital']
        c.latitude = country['latitude']
        c.longitude = country['longitude']

        c.objects.create()
    return Response(json.loads(countries.content))




