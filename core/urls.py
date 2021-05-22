from django.urls import path
from .views import (
    index,
    doctor,
    get_doctor,
    search_doctor,
    init_world
)

urlpatterns = [
    path('',index,name='index'),
    path('doctor/',doctor,name="doctor"),
    path('get_doctor/',get_doctor,name="Get Doctor"),
    path('search/',search_doctor,name="Search Doctor"),
    path('init/',init_world,name='init world')
]