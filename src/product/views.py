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

def product_detail(request, id=None):
    #instance = product.objects.get(id=1)
    instance = get_object_or_404(product, id=id)
    context = {
        "title": instance.author,
        "instance": instance,
    }
    return render(request, "product_detail.html", context)

