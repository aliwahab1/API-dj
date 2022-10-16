from django.contrib import admin

# Register your models here.

from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display=('fullname',  'email', 'subject', 'phone', 'message', 'date')
    list_filter=('fullname', 'date')


admin.site.register(Contact, ContactAdmin)