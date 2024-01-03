from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, OrderSerializer
from .models import Product, Order

class ProductAPI(APIView):

    def get(self, request):
        try:
            product_id = request.query_params.get('product_id')          

            if product_id:
                product = get_object_or_404(Product, id=product_id)
                serializer = ProductSerializer(product, many = False)
                return Response({
                "success": True,
                "message": f"Product Details for {product.name}",
                "response": serializer.data,
                }, status=status.HTTP_200_OK)
            else:
                product = Product.objects.all()
                serializer = ProductSerializer(product, many = True)
                return Response({
                    "success": True,
                    "message": f"All Products",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Product created successfully",
                        "response": ProductSerializer(product).data,  # Serialize the created instance
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        try:
            product_id = request.query_params.get('product_id')

            if not product_id:
                return Response(
                    {"success": False, "message": "No Product ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            product = get_object_or_404(Product, id=product_id)

            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Product Updated successfully",
                        "response": ProductSerializer(product).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        try:
            product_id = request.query_params.get('product_id')

            if not product_id:
                return Response(
                    {"success": False, "message": "No Product ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            product = get_object_or_404(Product, id=product_id)
    
            product.delete()
    
            return Response(
                {"success": True, "message": "Product Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class OrderAPI(APIView):
    def get(self, request):
        try:
            order_id = request.query_params.get('order_id')          

            if order_id:
                order = get_object_or_404(Order, id=order_id)
                serializer = OrderSerializer(order, many=False)
                return Response({
                    "success": True,
                    "message": f"Order Details for {order_id}",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)
            else:
                orders = Order.objects.all()  # Corrected this line
                serializer = OrderSerializer(orders, many=True)  # Corrected this line
                return Response({
                    "success": True,
                    "message": f"All Orders",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)
           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity')

            if not product_id or not quantity:
                return Response(
                    {"success": False, "message": "Product ID and Quantity are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            product = get_object_or_404(Product, id=product_id)

            if product.stock_quantity < quantity:
                return Response(
                    {"success": False, "message": "Not enough Stock Quantity, try ordering for a lesser quantity"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            total_price = quantity * product.price
            order = Order.objects.create(product=product, quantity=quantity, total_price=total_price)

            product.stock_quantity -= quantity
            product.save()

            serializer = OrderSerializer(order)
            return Response({
                "success": True,
                "message": "Order created successfully",
                "response": serializer.data,
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"success": False,
                 "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)

