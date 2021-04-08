import re

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from users.models import Passport


def register(request):
    return render(request, 'users/register.html')


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    if not all([username, password, email]):
        return render(request, 'users/register.html', {'errmsg': '参数不能为空！'})

    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'users/register.html', {'errmsg': '邮箱不合法！'})

    try:
        Passport.objects.add_one_passport(username=username, password=password, email=email)
    except Exception as e:
        print("e: ", e)
        return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})

    return redirect(reverse('book:index'))


def login(request):
    if request.COOKIES.get("username"):
        username = request.COOKIES.get("username")
        checked = 'checked'
    else:
        username = ''
        checked = ''
    context = {
        'username': username,
        'checked': checked,
    }

    return render(request, 'users/login.html', context)
