from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
class Base(View):
    view = {}


class HomeView(Base):

    def get(self,request):
        return render(request, 'index.html')