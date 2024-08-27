from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    products = models.ManyToManyField(Product)
