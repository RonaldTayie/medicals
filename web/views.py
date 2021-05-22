from django.shortcuts import render

from account.models import Account
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.views import APIView
# Create your views here.

def index(request):
    return render(request, 'default/index.html',)