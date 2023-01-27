from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list_view, name='list')
]
