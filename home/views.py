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
        ids = Brand.objects.get(slug=slug).id
        view = {}   
        self.views['product_brand'] = Product.objects.filter(brand_id=ids)
        return render(request, 'brand.html', self.views)