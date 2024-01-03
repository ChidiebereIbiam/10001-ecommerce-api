from django.urls import path
from .views import ProductAPI, OrderAPI

urlpatterns = [
    path('product/', ProductAPI.as_view()),
    path('order/', OrderAPI.as_view())
]
