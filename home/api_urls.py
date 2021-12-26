from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('items', ProductListView.as_view())
]