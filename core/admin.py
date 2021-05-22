from django.contrib import admin
from .models import (
    City,
    State,
    Contact,
    Country,
    Doctor,
    DoctorCategory,
    DoctorQualification,
    DoctorRegistration,
    Location,
    Practice,
    PracticeRegistration,
)
 
# ------------Location---------------

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('lid', 'country','state','city')
    list_filter =  ('lid','country','state','city')
    fieldsets = (
        (None, {'fields': ('lid', 'country','state','city')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('lid', 'country','state','city')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('lid', 'country','state','city')
    ordering = ('lid','country','state','city')

admin.site.register(Location, LocationAdmin)

# ------------Doctor-----------------

# Doctor Admin

class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ('user', 'description',)
    list_filter =  ('user','description')
    fieldsets = (
        (None, {'fields': ('user', 'description',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('user', 'description',)
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('user', 'description',)
    ordering = ('user','description')

admin.site.register(Doctor, DoctorAdmin)

# Doctor Registration

class DoctorRegistrationAdmin(admin.ModelAdmin):
    model = DoctorRegistration
    list_display = ('doctor', 'reg_num','reg_status','register','reg_board')
    list_filter =  ('reg_status','register','reg_board')
    fieldsets = (
        (None, {'fields': ('doctor', 'reg_num','reg_status','register','reg_board')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('doctor', 'reg_num','reg_status','register','reg_board')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('doctor', 'reg_num','reg_status','register','reg_board')
    ordering = ('reg_status','register','reg_board')

admin.site.register(DoctorRegistration, DoctorRegistrationAdmin)

# Doctor Qualification Admin

class DoctorQualificationAdmin(admin.ModelAdmin):
    model = DoctorQualification
    list_display = ('doctor', 'qualification_name','date_obtained')
    list_filter =  ('doctor','qualification_name','date_obtained')
    fieldsets = (
        (None, {'fields': ('doctor', 'qualification_name','date_obtained')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('doctor', 'qualification_name','date_obtained')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('doctor', 'qualification_name','date_obtained')
    ordering = ('doctor','qualification_name','date_obtained')

admin.site.register(DoctorQualification, DoctorQualificationAdmin)

# Doctor Category Admin

class DoctorCategoryAdmin(admin.ModelAdmin):
    model = DoctorCategory
    list_display = ('doctor', 'c_type','field','speciality','sub_speciality','start_date','origin')
    list_filter =  ('c_type','speciality','sub_speciality','origin')
    fieldsets = (
        (None, {'fields': ('doctor', 'c_type','field','speciality','sub_speciality','start_date','origin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('doctor', 'c_type','field','speciality','sub_speciality','start_date','origin')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('doctor', 'c_type','field','speciality','sub_speciality','start_date','origin')
    ordering = ('doctor','c_type','field','speciality','start_date','origin')

admin.site.register(DoctorCategory,DoctorCategoryAdmin)

# -----------Practice---------------

# Practice Admin
class PracticeAdmin(admin.ModelAdmin):
    model = Practice
    list_display = ('doctor', 'name',)
    list_filter =  ('doctor','name')
    fieldsets = (
        (None, {'fields': ('doctor', 'name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('doctor', 'name',)
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('doctor', 'name',)
    ordering = ('doctor','name')

admin.site.register(Practice,PracticeAdmin)

# Practice Registration Admin

class PracticeRegistrationAdmin(admin.ModelAdmin):
    model = PracticeRegistration
    list_display = ('practice', 'reg_num','reg_date','status')
    list_filter =  ('practice','reg_num','reg_date','status')
    fieldsets = (
        (None, {'fields': ('practice', 'reg_num','reg_date','status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('practice', 'reg_num','reg_date','status')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('practice','reg_date','status')
    ordering = ('practice','reg_num','reg_date','status')

admin.site.register(PracticeRegistration,PracticeRegistrationAdmin)

# Country

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('name', 'iso3','iso2','phone_code','capital','latitude','longitude')
    list_filter =  ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'iso3','iso2','phone_code','capital','latitude','longitude')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('name', 'iso3','iso2','phone_code','capital','latitude','longitude')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('name', 'iso3','iso2','phone_code','capital',)
    ordering = ('name','iso3','iso2','phone_code')

admin.site.register(Country,CountryAdmin)

# State
class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ('country', 'country_code','state_code','name',)
    list_filter =  ('country','state_code','name')
    fieldsets = (
        (None, {'fields': ('country', 'country_code','name','state_code',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('country', 'country_code','state_code','name',)
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('country','name',)
    ordering = ('country','state_code','name')

admin.site.register(State,StateAdmin)

# City
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'state','latitude','longitude')
    list_filter =  ('name','state','latitude','longitude')
    fieldsets = (
        (None, {'fields': ('name', 'state','latitude','longitude')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('name', 'state','latitude','longitude')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('name','state','latitude','longitude')
    ordering = ('name','state','latitude','longitude')

admin.site.register(City,CityAdmin)

# ---------Contact-------------

class ContactAdmin (admin.ModelAdmin):
    model = Contact
    list_display = ('isDoctor', 'account','practice','phone','location','address')
    list_filter =  ('isDoctor','account','practice',)
    fieldsets = (
        (None, {'fields': ('isDoctor', 'account','practice','location','address')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('isDoctor', 'account','practice','phone','location','address')
            }
        ),
    )
    filter_horizontal = []
    filter_vertical = []
    search_fields = ('isDoctor','account','practice','location')
    ordering = ('isDoctor','practice')

admin.site.register(Contact,ContactAdmin)



