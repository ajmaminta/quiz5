from django.contrib import admin  # Import the admin module
from django.urls import path, include
from . import views  # Import views.py for any additional routes you may want

urlpatterns = [
    path('', views.home, name='home'),  # Optional: if you want to show a home page, you can define this in views.py
    path('admin/', admin.site.urls),  # Admin URL for accessing the Django admin interface
    path('api/products/', include('products.urls')),  # Include URLs from the products app
    path('api/accounts/', include('accounts.urls')),  # Include URLs from the accounts app
]
