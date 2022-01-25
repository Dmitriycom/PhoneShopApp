from django.contrib import admin
from django.urls import re_path, path
from main import views

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', views.index, name='home'),
    re_path(r'^product$', views.product, name='product'),
    re_path(r'^reviews$', views.reviews, name='reviews'),
    re_path(r'^about$', views.about, name='about'),
]
