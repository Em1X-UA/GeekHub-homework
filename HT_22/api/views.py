from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions, viewsets

from product.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
