from django.shortcuts import render
from .models import TopPhone, ImageCarousel, ProductCatalog


def index(request):
    phones = TopPhone.objects.all()
    firstimg = ImageCarousel.objects.first
    return render(request, "main/index.html", {'phones': phones, "firstimg": firstimg })


def product(request, productid=1):
    id = "<h2>Product № {0}</h2>".format(productid)
    id = 1 
    phone = ProductCatalog.objects.get(pk=id)
    return render(request, "main/product.html", {"phone":phone})

    
def reviews(request):
    return render(request, "main/reviews.html")


def about(request):
    return render(request, "main/about.html")

