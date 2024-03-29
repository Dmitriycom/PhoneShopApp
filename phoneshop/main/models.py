from ast import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

class TopPhone(models.Model):
    url = models.URLField('Ссылка')
    name = models.CharField('Название', max_length=50)
    cost = models.IntegerField('Цена')
    urltoprodust = models.CharField('Ссылка к товару', default="product", max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Популярный телефон'
        verbose_name_plural = 'Популярные телефоны'


class ImageCarousel(models.Model):
    url = models.URLField('Ссылка')
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)


class ProductCatalog(models.Model):
    url = models.URLField('Ссылка')
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    cost = models.IntegerField('Цена')

    def __str__(self) -> str:
        return self.url
    
    class Meta:
        verbose_name = 'Каталог товара'
        verbose_name_plural = 'Каталог товара'


class Comment(models.Model):
    name = models.CharField('Имя', max_length=30)
    date = models.DateField('Дата')
    grade = models.IntegerField('Оценка')
    description = models.TextField('Описание', max_length=250)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

