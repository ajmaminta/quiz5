# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='get_products'),
    path('products/<int:product_id>/', views.get_product, name='get_product'),
]
