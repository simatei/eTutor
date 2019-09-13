from django.shortcuts import render
from rest_framework import generics

from tutor.models import TutorProfile, StudentProfile
from tutor.serializers import TutorProfileSerializer, StudentProfileSerializer


# Create ListCreateApiView() for TutorProfileSerializer
class TutorListCreate(generics.ListCreateAPIView):
    queryset = TutorProfile.objects.all()
    serializer_class = TutorProfileSerializer


# Create ListCreateApiView() for StudentProfileSerializer
class StudentListCreate(generics.ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
