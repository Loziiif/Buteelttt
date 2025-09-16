from django.contrib import admin
from .models import Category, Product

# Category Admin
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')       # Admin дээр баганаар харагдах зүйл
    search_fields = ('name',)           # Хайлтын талбар

# Product Admin
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'stock')  # Admin-д харагдах баганууд
    list_filter = ('category',)                                  # Category-аар шүүх боломж
    search_fields = ('title', 'description')                     # Хайлтын талбар
