from rest_framework import serializers
from .models import Contact

class ContatctSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['fullname', 'email', 'subject', 'phone', 'message']