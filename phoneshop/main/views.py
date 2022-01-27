from math import prod
from django.shortcuts import render
from .models import TopPhone, ImageCarousel, ProductCatalog


def index(request):
    phones = TopPhone.objects.all()
    firstimg = ImageCarousel.objects.first
    return render(request, "main/index.html", {'phones': phones, "firstimg": firstimg })


def product(request, productid=1):
    try:
        id = int(productid)
        phone = ProductCatalog.objects.get(pk=id)
    except:
        id = 1
        phone = ProductCatalog.objects.get(pk=id)
    phones = ProductCatalog.objects.exclude(pk=id)
    return render(request, "main/product.html", {"phone":phone, "phones": phones})

    
def reviews(request):
    return render(request, "main/comments.html")


def about(request):
    return render(request, "main/about.html")

