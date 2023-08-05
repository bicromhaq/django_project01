from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name= "home"),
    path('content', views.content, name= "content"),
]