from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('hello', hello),
    path('get_all_categories', getAllCategories),
    path('search_products', searchProducts),
    path('product/<id>', getProduct),
    path('api/token', jwt_views.TokenObtainPairView.as_view()),
]