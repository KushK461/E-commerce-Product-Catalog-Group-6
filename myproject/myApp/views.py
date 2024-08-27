from rest_framework import viewsets
from django.shortcuts import render
from .models import Category, Brand, Product, Review, Order
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, ReviewSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def home(request):
    context={}
    return render(request, "myApp/home.html",context)

def products(request):
    context={}
    return render(request, "myApp/products.html",context)
    