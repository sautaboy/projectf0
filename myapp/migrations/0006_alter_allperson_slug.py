# Generated by Django 4.1.7 on 2023-06-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_allperson_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allperson',
            name='slug',
            field=models.SlugField(),
        ),
    ]
