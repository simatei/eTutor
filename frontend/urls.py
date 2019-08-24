from django.urls import path

from . import views

# views
urlpatterns = [
    path('', views.index)
]