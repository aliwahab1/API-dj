from django.db import models

# Create your models here.

class Registered_student(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    center=models.CharField(max_length=200, null=True)
    course=models.CharField(max_length=200, null=True)
    mode=models.CharField(max_length=200, null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    