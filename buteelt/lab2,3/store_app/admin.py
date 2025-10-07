from django.contrib import admin
from store_app.models import Baraa,Angilal

class BaraaSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('bname',)}

class AngilalSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('aname',)}


admin.site.register(Baraa, BaraaSlug)
admin.site.register(Angilal, AngilalSlug)
