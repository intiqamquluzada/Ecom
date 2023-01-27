# Generated by Django 3.2 on 2022-12-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('colors', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Brown', 'Brown'), ('Gray', 'Gray'), ('Orange', ' Orange'), ('Green', 'Green')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='color',
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.ManyToManyField(blank=True, to='products.Color'),
        ),
    ]
