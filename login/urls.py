# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.index_view),
    url(r'^login/',views.index_view),

]