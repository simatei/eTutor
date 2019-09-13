from rest_framework import serializers

from tutor.models import TutorProfile, StudentProfile


# Tutor Profile serializer
class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorProfile
        fields = ('id', 'first_name', 'last_name', 'specialization')


# Student Profile Serializer
class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'first_name', 'last_name', 'department')
