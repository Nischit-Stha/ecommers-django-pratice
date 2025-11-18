from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *


# Create your views here.
class Base(View):
    pass


class HomeView(Base):

    def get(self, request):
        view = {}
        view['categories'] = Category.objects.all()
        view['sliders'] = Slider.objects.all()
        view['ads'] = AD.objects.all()
        view['brands'] = Brand.objects.all()
        view['customers'] = Customer.objects.all()
        view['products'] = Product.objects.all()
        view['hots'] = Product.objects.filter(labels='hot')
        view['news'] = Product.objects.filter(labels='new')
        return render(request, 'index.html', view)


class CategoryView(Base):

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        view = {}
        view['category'] = category
        view['product_category'] = Product.objects.filter(category=category)
        return render(request, 'category.html', view)
    

class BrandView(Base):

    def get(self, request, slug):
        brand = get_object_or_404(Brand, slug=slug)
        view = {}
        view['brand'] = brand
        view['product_brand'] = Product.objects.filter(brand=brand)
        return render(request, 'brand.html', view)
    

class ProductDetailView(Base):

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        view = {}
        view['product'] = product
        return render(request, 'product-detail.html', view)
    

class SearchView(Base):

    def get(self, request):
        query = request.GET.get('query')
        view = {}
        view['search_products'] = Product.objects.filter(name__icontains=query)
        view['query'] = query
        return render(request, 'search.html', view)