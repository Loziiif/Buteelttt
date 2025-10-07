from django.shortcuts import render
from .models import Baraa, Angilal


def show_baraa_form(request):
    
    return render(request, "baraa.html")


def index(request):
    return render(request, "index.html")


def show_cart(request):
    return render(request, "cart.html")


def show_dashboard(request):
    return render(request, "dashboard.html")


def show_order_complete(request):
    return render(request, "order_complete.html")


def show_place_order(request):
    return render(request, "place-order.html")


def show_product_detail(request):
    return render(request, "product-detail.html")


def show_register(request):
    return render(request, "register.html")


def show_search(request):
    return render(request, "search-result.html")


def show_signin(request):
    return render(request, "signin.html")


def show_store(request):
    return render(request, "store.html")


def show(request):
    pass