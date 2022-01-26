from django.shortcuts import render
from .models import TopPhone, ImageCarousel


def index(request):
    phones = TopPhone.objects.all()
    firstimg = ImageCarousel.objects.first
    return render(request, "main/index.html", {'phones': phones, "firstimg": firstimg })


def product(request):
    return render(request, "main/product.html")

    
def reviews(request):
    return render(request, "main/reviews.html")


def about(request):
    return render(request, "main/about.html")