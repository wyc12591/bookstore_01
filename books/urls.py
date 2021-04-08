from django.urls import path, re_path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'books/(?P<books_id>\d+)', views.detail, name='detail'),
]
