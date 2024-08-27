from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, ReviewViewSet, OrderViewSet

#We are registering my viewsets with the router,#
# so that we can create the correct URL patterns#
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
   path('', include(router.urls)),

     ]

    