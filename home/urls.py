from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]

# Serve static files during development