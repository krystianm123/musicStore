from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import news
from django.utils import timezone
# Create your views here.



def news_list(request):
    queryset = news.objects.all()
    context = {
        "object2_list": queryset,
        "title": "list news"
    }
    return render(request, 'news_list.html', context)