from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('single_s/', views.single_s, name='single_s'),
]