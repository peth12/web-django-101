from django.urls import path
from web_django_app import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('form', views.form),
    
]
