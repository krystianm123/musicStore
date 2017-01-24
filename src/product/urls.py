from django.conf.urls import url

from .views import (
    product_list,
    product_detail
)
urlpatterns = [
    # ex: /polls/
    url(r'^$', product_list),
    url(r'^(?P<id>\d+)/$', product_detail, name='detail'),



]