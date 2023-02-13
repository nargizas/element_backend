from django.shortcuts import render
from django.http import JsonResponse
from . import models

# Create your views here.


def get_all_products(request):
    products = models.Product.objects.all()
    products_list = [
        {
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "amount": p.amount,
            "is_active": p.is_active,
        }
        for p in products
    ]
    return JsonResponse(products_list, safe=False)


def get_product_by_id(request, *args, **kwargs):
    product = models.Product.objects.get(id=int(kwargs["id"]))
    product_info = {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "amount": product.amount,
        "is_active": product.is_active,
    }
    return JsonResponse(product_info, safe=False)


def get_all_categories(request):
    categories = models.Category.objects.all()
    categories_list = [
        {
            "name": c.name,
        }
        for c in categories
    ]
    return JsonResponse(categories_list, safe=False)


def get_category_by_id(request, *args, **kwargs):
    category = models.Category.objects.get(id=int(kwargs["id"]))
    category_info = {
        "name": category.name,
    }
    return JsonResponse(category_info, safe=False)


def get_product_by_category(request, *args, **kwargs):
    category = models.Category.objects.get(id=int(kwargs["id"]))
    products = category.product_set.all()
    products_list = [
        {
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "amount": p.amount,
            "is_active": p.is_active,
        }
        for p in products
    ]
    return JsonResponse(products_list, safe=False)
