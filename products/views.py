# products/views.py

from django.http import JsonResponse
from .models import Product  # This import should work fine

def get_products(request):
    products = Product.objects.all()
    product_data = []
    for product in products:
        product_data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'image': product.image.url if product.image else None,
            'brand': product.brand,
            'category': product.category,
            'description': product.description,
            'rating': product.rating,
            'numReviews': product.numReviews,
        })
    return JsonResponse(product_data, safe=False)

def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'image': product.image.url if product.image else None,
            'brand': product.brand,
            'category': product.category,
            'description': product.description,
            'rating': product.rating,
            'numReviews': product.numReviews,
        }
        return JsonResponse(product_data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
