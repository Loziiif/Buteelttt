from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin) # type: ignore


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product, ProductAdmin) # type: ignore