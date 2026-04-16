from django.urls import path
from .views import generate_videos

urlpatterns = [
    path('generate_videos/', generate_videos, name='generate_videos'),
]