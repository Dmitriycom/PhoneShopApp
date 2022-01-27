# Generated by Django 4.0.1 on 2022-01-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_decription_imagecarousel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Каталог товара',
                'verbose_name_plural': 'Каталог товара',
            },
        ),
    ]