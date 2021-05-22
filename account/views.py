from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from account.serializers import UserSerializer
from django.forms.models import model_to_dict
from .decorators import *

from rest_framework.authtoken.models import Token

# Signup View
@api_view(['POST'])
def signUp(request):
    if request.method =='POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data = {
                'email':account.email,
                'username':account.username,
            }
            data['response']  = "Signup Success"
            token = Token.objects.get(user=account).key
            data['Token'] = token
        else:
            print("Data is invalid")
            data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@allowed_groups(['admin','doctor','user'])
def accountDetails(request):
    user = request.user
    if user.groups.exists():
        group = user.groups.all()[0].name
        # update groups element in user
        user._mutable = False
        u = model_to_dict(user,exclude=['password','user_permissions','is_superuser','is_staff','last_login'])
        u['groups'] = group
        return Response(u)
    return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET'])
def AccountOverview(request):
    sheet = {
        "Account":{
            "signIn":"signIn",
            "signUp":"signUp",
        }
    }
    return Response(sheet)