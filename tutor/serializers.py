from rest_framework import serializers

from tutor.models import TutorProfile

class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorProfile
        fields = ('id', 'first_name', 'last_name', 'specialization')