from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
]

# Serve static files during development