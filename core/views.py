
import json

from pathlib import Path
import os

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
import json

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
    doctors = Doctor.objects.all()
    docs = []
    for doctor in doctors:
        doctor._mutable = False
        doc = model_to_dict(doctor)
        doc['user'] = acc_to_dict(doctor.user)
        docs.append(doc)

    return Response(docs)

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

# ====================================================================
# ==================    I   N   I   T   ==============================
# ====================================================================

def load_countries(data_file_dir):
    c = open(file=data_file_dir,encoding='utf-8')
    country_data = json.load(c)

    countries = []
    for c in country_data:
        country = {
            'name':c['name'],
            'iso3':c['iso3'],
            'iso2':c['iso2'],
            'phone_code':c['phone_code'],
            'capital':c['capital'],
            'latitude':c['latitude'],
            'longitude':c['longitude']
        }
        Data = Country(**country)
        Data.save()
    

def load_States(data_file_dir):
    s = open(file=data_file_dir,encoding='utf-8')
    states_data = json.load(s)
    for st in states_data:
        c = Country.objects.get(iso2=st['country_code'])
        S = {
            'country':c,
            'country_code':st['country_code'],
            'name':st['name'],
            'state_code':st['state_code']
        }
        state = State(**S)
        print(state)
        state.save()

def load_Cities(data_file_dir):
    city_file = open(file=data_file_dir,encoding='utf-8')
    city_data = json.load(city_file)

    for city in city_data:
        c = State(**city)
        print(c)


@api_view(['GET'])
def init_world(request):
    current_dir = os.path.dirname(__file__)
    country_file = "countries.json"
    states_file = "states.json"
    cities_file = "cities.json"

    # countries_file_dir = os.path.join(current_dir,"init",country_file)
    # countries = load_countries(countries_file_dir)

    # countries_file_dir = os.path.join(current_dir,"init",states_file)
    # States = load_States(countries_file_dir)

    cities_data_file = os.path.join(current_dir,"init",cities_file)
    cities = load_Cities(cities_data_file)

    return Response([])




