from django.contrib import admin
from .models import *


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    max_num = 10


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    inlines = [ImageInline]
    list_display = ('category', 'name')
    list_filter = ('created_at',)
    search_fields = ('category', 'name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(Size)
admin.site.register(Color)
