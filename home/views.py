from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
class Base(View):
    view = {}


class HomeView(Base):

    def get(self,request):
        self.view['categories'] = Category.objects.all()
        self.view['sliders'] = Slider.objects.all()
        self.view['ads'] = AD.objects.all()
        self.view['brands'] = Brand.objects.all()
        self.view['customers'] = Customer.objects.all()
        self.view['products'] = Product.objects.all()   
        return render(request, 'index.html')