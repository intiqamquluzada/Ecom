from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from services.mixin import DateMixin, SlugMixin
from services.uploader import Uploader
from services.generator import Generator
from services.Size import SIZES
from services.color import COLOR


class Size(DateMixin):
    sizes = models.CharField(max_length=100, choices=SIZES)

    def __str__(self):
        return self.sizes


class Color(DateMixin):
    colors = models.CharField(max_length=100, choices=COLOR)

    def __str__(self):
        return self.colors


class Category(MPTTModel, DateMixin, SlugMixin):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to=Uploader.upload_images_to_categories, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = Generator.create_slug_shortcut(size=20, model_=Category)
        super(Category, self).save(*args, **kwargs)


class Product(DateMixin, SlugMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200)
    description = RichTextField()
    price = models.FloatField()
    tax = models.FloatField(null=True, blank=True, default=0)
    discount = models.FloatField(null=True, blank=True, default=0)
    sizes = models.ManyToManyField(Size, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.slug = Generator.create_slug_shortcut(size=20, model_=Product)
        super(Product, self).save(*args, **kwargs)


class ProductImage(DateMixin, SlugMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.upload_images_to_products)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def save(self, *args, **kwargs):
        self.slug = Generator.create_slug_shortcut(size=20, model_=ProductImage)
        super(ProductImage, self).save(*args, **kwargs)
