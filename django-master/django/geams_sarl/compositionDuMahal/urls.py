from django.urls import path
from . import views

urlpatterns = [
    path('r^$', views.index, name='index'),
    path('r^detail/$', views.detail, name='detail'),
    path('r^search/$', views.search, name='search'),
]
