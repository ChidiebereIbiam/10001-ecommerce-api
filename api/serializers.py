from rest_framework.serializers import ModelSerializer
from .models import Product, Order

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'total_price', 'product_details']