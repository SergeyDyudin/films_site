# Generated by Django 3.1.4 on 2021-01-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_films_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='main/icons', verbose_name='Иконка'),
        ),
    ]
