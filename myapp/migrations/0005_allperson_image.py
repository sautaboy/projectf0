# Generated by Django 4.1.7 on 2023-06-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_allperson_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='allperson',
            name='image',
            field=models.ImageField(default='upload-image', upload_to='myapp/images'),
        ),
    ]
