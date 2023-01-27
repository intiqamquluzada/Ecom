# Generated by Django 3.2 on 2022-12-25 12:48

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=services.uploader.Uploader.upload_images_to_products),
        ),
    ]
