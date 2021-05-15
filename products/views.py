from django.shortcuts import render
from .models import Products

# Create your views here.

def products(request):
    all_products = Products.objects.all()
    return render(request,'products/products.html',{"products": all_products})

def product_detail(request,slug):
    product = Products.objects.get(slug=slug)
    print(product)
    return render(request,"products/product-details.html",{"product": product})