from django.contrib import admin

# Register your models here.

from .models import *



class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name',  'email', 'phone',  'date', 'course', 'center', 'mode', 'address')
    list_filter=('first_name', 'last_name', 'date', 'course', 'center', 'mode')


admin.site.register(Registered_student, StudentAdmin)