from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(),name = 'home'),
    path('category/<slug>', CategoryView.as_view(), name = 'category'),
    path('product/<slug>', DetailView.as_view(), name = 'product'),
    path('search', SearchView.as_view(), name = 'search'),
    path('signup', signup, name = 'signup'),
]