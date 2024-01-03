from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer
from .models import Product
import json


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

