from django.db import models


# Department Table
class Department(models.Model):
    DEPARTMENTS = [
        ('MA', 'Mathematics'),
        ('SC', 'Sciences'),
    ]
    department = models.CharField(max_length=30, choices=DEPARTMENTS)

    def __str__(self):
        return self.department


# Tutor Profile
class TutorProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    specialization = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Student Profile
class StudentProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    enrolled = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
