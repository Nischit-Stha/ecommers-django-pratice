from django.shortcuts import render
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
        category = Category.objects.get(slug=slug)
        view = {}
        view['category'] = category
        view['products'] = Product.objects.filter(category=category)
        return render(request, 'product-list.html', view)
        self.view['subcategories'] = SubCategory.objects.filter(category=self.view['category'])
        self.view['products'] = Product.objects.filter(category=self.view['category'])
        return render(request, 'category.html')