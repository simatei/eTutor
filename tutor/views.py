from django.shortcuts import render
from rest_framework import generics

from tutor.models import TutorProfile
from tutor.serializers import TutorProfileSerializer

# Create ListCreateApiView() for TutorProfileSerializer
class TutorListCreate(generics.ListCreateAPIView):
    queryset = TutorProfile.objects.all()
    serializer_class = TutorProfileSerializer

    
