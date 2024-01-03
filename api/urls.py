from django.urls import path
from .views import ProductAPI

urlpatterns = [
    path('product/', ProductAPI.as_view())
]
