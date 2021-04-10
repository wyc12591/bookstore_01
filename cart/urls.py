from django.urls import path

from cart import views

urlpatterns = [
    path('add/', views.cart_add, name='add'),  # 添加购物车数据
    path('count/', views.cart_count, name='count'),  # 获取用户购物车中商品的数量
    path('', views.cart_show, name='show'),  # 显示用户的购物车页面
    path('del/', views.cart_del, name='delete'),
    path('update/', views.cart_update, name='update'),
]
