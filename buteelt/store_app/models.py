from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        unique=True,
        default="Uncategorized"  # Хуучин мөрүүдэд default
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        default="uncategorized"
    )
    description = models.TextField(
        max_length=255,
        blank=True
    )
    cat_image = models.ImageField(
        upload_to='photos/categories',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        unique=True,
        default="Unnamed Product"  # Хуучин мөрүүдэд default
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=255,
        blank=True
    )
    cat_image = models.ImageField(
        upload_to='photos/products',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
