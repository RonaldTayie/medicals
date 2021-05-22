from rest_framework import serializers
from django.contrib.auth.models import Group

from account.models import Account as User

class UserSerializer(serializers.ModelSerializer):
    password2   = serializers.CharField(style={'input_type':'password'},write_only=True)
    # user_group = serializers.CharField(style={'input_type':'text'},write_only=True)
    class Meta:
        model = User
        fields  = ['email','username','password','password2','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def save(self):
        if self.validated_data['password'] ==self.validated_data['password2']:
            account = User(
                email = self.validated_data['email'],
                username = self.validated_data['username'],
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name']
            )
            account.save()
            return account
        else:
            return None