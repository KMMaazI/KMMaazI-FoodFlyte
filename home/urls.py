from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('chinese/', views.chinese, name='chinese'),
    path('desi/', views.desi, name='desi'),
    path('fastfood/', views.fastfood, name='fastfood'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
   
]