from django.urls import path
from .views import *

urlpatterns = [
    path('hello', hello),
    path('get_all_categories', getAllCategories),
    path('search_products', searchProducts),
]