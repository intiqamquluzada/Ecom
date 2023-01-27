from django.db.models import F
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def product_list_view(request):
    products = Product.objects.annotate(
            total_price=F('price') + F('tax') - F('discount')
        ).order_by('-created_at')

    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {
        'categories': Category.objects.order_by('-created_at'),
        'products': product_list,
        'paginator': paginator,
        'sizes': Size.objects.order_by('-created_at'),
        'colors': Color.objects.order_by('-created_at'),
    }
    return render(request, 'list.html', context)
