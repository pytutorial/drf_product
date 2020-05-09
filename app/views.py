from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllCategories(request):
    lst = Category.objects.all()
    serializer = CategorySerializer(lst, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def searchProducts(request):
    productList = Product.objects.all()
    queryParams = request.GET
    productName = queryParams.get('keyword')
    categoryId = queryParams.get('categoryId')
    priceRange = queryParams.get('priceRange')

    minPrice, maxPrice = None, None
    priceTable = {
        '1' : [None, 10],
        '2': [10, 15],
        '3': [15, 20],
        '4': [20, None]
    }
    if priceRange:
        minPrice, maxPrice = priceTable.get(priceRange)

    if productName:
        productList = productList.filter(name__contains=productName)
    
    if categoryId:
        productList = productList.filter(category__id=int(categoryId))

    if minPrice:
        productList = productList.filter(price__gte=minPrice*1e6)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice*1e6)

    serializer = ProductSerializer(productList, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def hello(request):
    return Response({"message": "Hello"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProduct(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

