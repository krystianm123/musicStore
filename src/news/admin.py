from django.contrib import admin
from .models import news

# Register your models here.
class newsAdmin(admin.ModelAdmin):
    class Meta:
        model = news

    list_display = ('author', 'title', 'created_date')
admin.site.register(news, newsAdmin)