# chat/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('user1/', views.user1, name='user1'),
    path('variant/', views.variant, name='variant'),
]

