# Generated by Django 4.0.1 on 2022-01-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Описание'),
        ),
    ]
