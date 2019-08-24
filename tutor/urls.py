from django.urls import path

from . import views

# Url Patterns
urlpatterns = [
    path('api/tutor/', views.TutorListCreate.as_view() ),
]