from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Registered_studentSerializer
from .models import Registered_student

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Registered_student.objects.all().order_by('-id')
    serializer_class=Registered_studentSerializer
