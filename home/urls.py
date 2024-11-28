from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('chinese/', views.chinese, name='chinese'),
    path('desi/', views.desi, name='desi'),
    path('fastfood/', views.fastfood, name='fastfood'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view,name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('restaurant/<str:restaurant_name>/', views.restaurant_menu, name='restaurant_menu'),
    path('search/', views.search_restaurant, name='search_restaurant'),
    path('place_order/<int:menu_item_id>/', views.place_order, name='place_order'),
    path('orders/', views.orders_list, name='orders_list'),
]