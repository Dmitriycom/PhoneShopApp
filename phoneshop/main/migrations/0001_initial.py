# Generated by Django 4.0.1 on 2022-01-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('cost', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]
