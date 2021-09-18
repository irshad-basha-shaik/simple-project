from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name='home'),
    path('booksmenu', views.booksmenu, name='home1'),
    path('newbooks', views.newbooks, name='home2'),
    path('savebook', views.SaveBook, name='home3'),
]