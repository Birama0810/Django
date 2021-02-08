from django.urls import path


from . import views

urlpatterns = [
    path('r^$', views.index),
    path('r^proposition', views.all_ourrs_propositions)
]
