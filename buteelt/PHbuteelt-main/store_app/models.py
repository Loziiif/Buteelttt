from django.db import models



class Angilal(models.Model):
    aname = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True)
    cat_img =models.ImageField(upload_to='photos/categories', blank=True)
    def __str__(self):
        return self.aname

class Baraa(models.Model):
    bname =  models.CharField(max_length=200)  
    angilal =  models.ForeignKey(Angilal, on_delete = models.CASCADE, default=0)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True)
    price = models.PositiveBigIntegerField(default=0)
    images = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.bname}({self.angilal})"
