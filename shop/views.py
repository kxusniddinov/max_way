import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Customer, Product, Order, OrderProduct
from . import services
from .forms import CustomerForm, OrderProductForm, OrderForm
from config.settings import MEDIA_ROOT
from .services import get_product_by_id, get_user_by_phone, get_orderproduct_by_id


def home_page(request):
    if request.GET:
        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)


def order_page(request):
    if request.GET:
        user = get_user_by_phone(request.GET.get("phone_number", 0))
        return JsonResponse(user)


