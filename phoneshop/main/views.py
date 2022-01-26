from django.shortcuts import render
from .models import TopPhone, ImageCarousel 


def index(request):
    phones = TopPhone.objects.all()
    firstimg = ImageCarousel.objects.first
    return render(request, "main/index.html", {'phones': phones, "firstimg": firstimg })


def product(request, productid=0):
    output = "<h2>Product № {0}</h2>".format(productid)
    return render(request, "main/product.html")

    
def reviews(request):
    return render(request, "main/reviews.html")


def about(request):
    return render(request, "main/about.html")

