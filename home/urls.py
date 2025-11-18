from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('product/<slug>', ProductDetailView.as_view(), name='product-detail'),
    path('search/', SearchView.as_view(), name='search'),
]
# Serve static files during development