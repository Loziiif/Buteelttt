from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm

def dashboard(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    products = Product.objects.select_related('category').all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # store_app/views.py
    return render(request, 'store_app/dashboard.html', {
        'form': form,
        'products': products,
        'categories': categories,
})

