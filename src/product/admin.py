from django.contrib import admin
from .models import product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    class Meta:
        model = product

    list_display = ('author', 'name', 'price')
admin.site.register(product, productAdmin)