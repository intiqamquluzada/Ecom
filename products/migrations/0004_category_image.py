# Generated by Django 3.2 on 2022-12-25 14:41

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221225_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_images_to_products),
        ),
    ]
