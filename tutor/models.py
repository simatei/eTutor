from django.db import models

# Tutor Profile
class TutorProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    specialization = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

