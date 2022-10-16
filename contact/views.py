from django.shortcuts import render


from rest_framework import viewsets
from .serializers import ContatctSerializer
from .models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by('-id')
    serializer_class=ContatctSerializer
