from django.urls import path
from .views import home_view, products_view, single_product_view
from .api.views import product_list_view

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('products/<int:product_id>/', single_product_view, name='single_product'),
    path('rest/products_list', product_list_view, name='product_list'),
]