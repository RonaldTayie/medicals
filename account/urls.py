from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from  .views import signUp

urlpatterns = [
    path('signup',signUp,name='Signup'),
    path('signin',obtain_auth_token,name="Obtain Login Token")
]