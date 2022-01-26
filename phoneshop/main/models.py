from ast import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

class TopPhone(models.Model):
    url = models.URLField('Ссылка')
    name = models.CharField('Название', max_length=50)
    cost = models.IntegerField('Цена')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Популярный телефон'
        verbose_name_plural = 'Популярные телефоны'


class ImageCarousel(models.Model):
    url = models.URLField('Ссылка')
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)