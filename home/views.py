from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels = 'new')
        return render(request, 'index.html', self.views)

class CategoryView(BaseView):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        return render(request, 'category.html', self.views)

class DetailView(BaseView):
    def get(self, request, slug):
        
        self.views['products_details'] = Product.objects.filter(slug = slug)
        return render(request, 'product-detail.html', self.views)

class SearchView(BaseView):
    def get(self, request):
        query = request.GET.get('query')
        if query is not None:
            # print(len(Product.objects.filter(name__icontains= query)))
            self.views['search_result'] = Product.objects.filter(name__icontains = query)

        elif len(Product.objects.filter(name__icontains = query)) == 0:
            self.views['no_result'] = "No Result Found"

        else:
            return redirect('/')    
    
        return render(request, 'search.html', self.views)        

def signup(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']  
        uname = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password']
        cpassword = request.POST['cpassword'] 

        if password == cpassword:
            if User.objects.filter(username = uname).exists():
                messages.error(request, 'The username is already taken')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'The email is already taken')
                return redirect('signup')

            else:
                data = User.objects.create_user(
                    first_name = f_name,
                    last_name = l_name,
                    username = uname,
                    email = email,
                    password = password
                ) 
                data.save()
                return redirect('/') 

        else:
            messages.error(request, 'Password does not match ')
            return redirect('signup')

    return render(request, 'signup.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name =name,
            email = email,
            subject = subject,
            message = message
            )
        data.save()
        email = EmailMessage(
                 subject,
                 message,
                 '',
                 [email],
              )       

        return render(request, 'contact.html')

#----------------------------API---------------------------

from .models import *
from .serializers import *
from rest_framework import viewsets

# ViewSets define the view behavior.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer