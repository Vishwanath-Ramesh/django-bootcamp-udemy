from os import name
from django.conf.urls import url

from app_1 import views

urlpatterns = [
    url(r'^$', views.index, name='help')
]