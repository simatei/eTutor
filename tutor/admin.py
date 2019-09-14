from django.contrib import admin

from .models import (TutorProfile, Department, StudentProfile,
                     Projects)

# Register your models here.
admin.site.register(TutorProfile)
admin.site.register(Department)
admin.site.register(StudentProfile)
admin.site.register(Projects)
