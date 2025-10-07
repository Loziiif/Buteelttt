# store_app/views.py
from django.shortcuts import render
from .models import Product, Category

def index(request):
    products = Product.objects.all()
    return render(request, 'store_app/index.html', {'products': products})


def store(request):
    # Бүх категориудыг авах
    categories = Category.objects.all()

    # Тухайн category-ийн products-ийг авах
    products = Product.objects.all()  # бүх бүтээгдэхүүн

    # Жишээ: тодорхой category-ийн бүтээгдэхүүн
    if categories.exists():
        first_category = categories.first()
        first_category_products = first_category.products.all()  # related_name ашигласан

    context = {
        'categories': categories,
        'products': products,
        'first_category_products': first_category_products if categories.exists() else [],
    }

    return render(request, 'store_app/store.html', context)

def cart(request):
    return render(request, 'store_app/cart.html')

def dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store_app/dashboard.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store_app/product_detail.html', {'product': product})

def register(request):
    return render(request, 'store_app/register.html')

def signin(request):
    return render(request, 'store_app/signin.html')

def search_result(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'store_app/search_result.html', {'results': results, 'query': query})

def order_complete(request):
    return render(request, 'store_app/order_complete.html')

def store_view(request):
    return render(request, 'store.html')
