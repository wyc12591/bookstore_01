from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_handle/', views.register_handle, name='register_handle'),
]
