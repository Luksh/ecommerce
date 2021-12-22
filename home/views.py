from django.shortcuts import render
from .models import *
from django.views.generic import View

# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get (self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels = 'new')

        return render(request,'index.html',self.views)