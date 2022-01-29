from django.shortcuts import render
from .models import TopPhone, ImageCarousel, ProductCatalog, Comment

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
    if request.method == "POST":
        comment = Comment()
        comment.name = request.POST.get('Name')
        comment.date = request.POST.get('Date')
        try:
            comment.grade = request.POST.get('rating') if int(request.POST.get('rating')) > 0 else 4    
        except:
            comment.grade = 3
        comment.description = request.POST.get('Comment')
        comment.save()
        comments = Comment.objects.all()
        return render(request, "main/comments.html", {"comments": comments})
    else:
        comments = Comment.objects.all()
        return render(request, "main/comments.html",  {"comments": comments})


def about(request):
    return render(request, "main/about.html")

