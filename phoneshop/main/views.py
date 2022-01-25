from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")


def product(request):
    return render(request, "main/product.html")


def reviews(request):
    return render(request, "main/reviews.html")


def about(request):
    return render(request, "main/about.html")