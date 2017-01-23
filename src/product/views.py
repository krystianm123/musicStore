from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import product

def product_list(request):
    queryset = product.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"

    }
    template = 'product_list.html'
    return render(request, template, context)

def product_detail(request):
    isinstance(get_object_or_404(product, id=1))
    context = {
        "title": "Detail"
    }
    return render(request, "product_list.html", context)

