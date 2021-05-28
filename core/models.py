from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
unique_id = uuid.uuid4()
from django.conf import settings

class Timezone(models.Model):
    zone_name = models.CharField(max_length=30,unique=True,default='Zone Name')
    gmt_offset = models.IntegerField(default=0,null=False)
    gmt_offsetname = models.CharField(max_length=30,unique=True,default='UTC=00:00')
    abbreviation = models.CharField(max_length=4,unique=True,default='ABBR')
    tz_name = models.CharField(max_length=50,unique=True,default='TimeZone Name')

    def __str__(self):
        return str(self.zone_name)

# Country Model
class Country (models.Model):
    name = models.CharField(max_length=60,unique=True,default='')
    iso3 = models.CharField(max_length=3,unique=True,default='c3')
    iso2 = models.CharField(max_length=2,unique=True,default='c2')
    phone_code = models.CharField(max_length=4,default='+000')
    capital = models.CharField(max_length=60,default='')

    latitude = models.CharField(max_length=40,default='00.000000000')
    longitude = models.CharField(max_length=40,default='00.000000000')

    def __str__(self):
        return str(self.name)

# Province Model
class State (models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,)
    country_code = models.CharField(max_length=4,default='AAA',null=False,unique=False,blank=False)
    name = models.CharField(max_length=90,default='province')
    state_code = models.CharField(max_length=8,default='StCd')

    def __str__(self):
        return self.name

# City Model
class City (models.Model):
    name = models.CharField(max_length=90,null=False,default='city',blank=False)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE,default="",)
    state = models.ForeignKey(State,on_delete=models.CASCADE,default="",)

    latitude = models.CharField(max_length=40,unique=True,default='00.000000000')
    longitude = models.CharField(max_length=40,unique=True,default='00.000000000')

    def __str__(self):
        return ''

# Consolidate the country province and city into one searchable object for the practise as location
class Location(models.Model):
    # Location ID [lid]
    lid = models.UUIDField(default=uuid.uuid4(), blank=False,unique=True,unique_for_date=True,auto_created=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,)
    state = models.ForeignKey(State,on_delete=models.CASCADE,)
    city = models.ForeignKey(City,on_delete=models.CASCADE,)

    def __str__(self):
        return ''

# Record Status

class Status(models.Model):
    name = models.CharField(default='Active',unique=True,null=False,blank=False,max_length=10)

    def __str__(self):
        return self.name

# -----------DOCTOR------------------------

# Doctor & Practise
class Doctor (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.user.first_name

# Doctor Registration data
class DoctorRegistration (models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,)
    reg_num = models.CharField(max_length=20,unique=True,default='Reg Number')
    reg_status = models.BooleanField(default=False)
    register = models.CharField(max_length=127,unique=True,default='Register')
    reg_board = models.CharField(max_length=127,default='Board')

    def __str__(self):
        return self.doctor

# basic information on the doctors' Qualification
class DoctorQualification(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,)
    qualification_name = models.CharField(max_length=100,unique=False,default='')
    date_obtained = models.DateField(auto_now=False,)

    def __str__(self):
        return "%s %s"%(self.doctor , self.qualification_name)

# the category or firld in which the doctor Work
class DoctorCategory (models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    c_type = models.CharField(max_length=50,unique=True,default='Practice Type')
    field = models.CharField(max_length=60,default='Practice Field')
    speciality = models.CharField(max_length=90,default='Practice Speciality',blank=False)
    sub_speciality = models.CharField(max_length=90,default="")

    start_date = models.DateField(auto_now=False)
    origin = models.ForeignKey(Country,on_delete=models.SET_DEFAULT,default='')

    def __str__(self):
        return self.doctor+" "+self.c_type

# ----------Practice------------

# Practice [clinic,hospital, etc...]
class Practice (models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=False,default='')
    logo = models.ImageField(_('Practice Logo'),upload_to="logo")
    description = models.TextField()

# Practice Registration Data
class PracticeRegistration(models.Model):
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE)
    reg_num = models.CharField(max_length=30,null=False,default='Reg Number')
    reg_date = models.DateField(auto_now=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.practice

# ------------Contacts---------------------

# Contact Details of the doctor or  a practice
class Contact(models.Model):
    # is the user or record is of a doctor then the isDoctor will be true
    isDoctor = models.BooleanField(default=False)
    # only one can have a value
    account = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE,null=True,blank=True)

    phone = models.CharField(max_length=20,null=False,blank=True),
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        if(not self.doctor):
            return self.practice
        return self.doctor



