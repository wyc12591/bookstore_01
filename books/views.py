from django.core.paginator import Paginator
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from books.enums import PYTHON, JAVASCRIPT, ALGORITHMS, MACHINELEARNING, OPERATINGSYSTEM, DATABASE, BOOKS_TYPE
from books.models import Books


def index(request):
    python_new = Books.objects.get_books_by_type(PYTHON, limit=3, sort='new')
    python_hot = Books.objects.get_books_by_type(PYTHON, limit=4, sort='hot')
    javascript_new = Books.objects.get_books_by_type(JAVASCRIPT, limit=3, sort='new')
    javascript_hot = Books.objects.get_books_by_type(JAVASCRIPT, limit=4, sort='hot')
    algorithms_new = Books.objects.get_books_by_type(ALGORITHMS, 3, sort='new')
    algorithms_hot = Books.objects.get_books_by_type(ALGORITHMS, 4, sort='hot')
    machinelearning_new = Books.objects.get_books_by_type(MACHINELEARNING, 3, sort='new')
    machinelearning_hot = Books.objects.get_books_by_type(MACHINELEARNING, 4, sort='hot')
    operatingsystem_new = Books.objects.get_books_by_type(OPERATINGSYSTEM, 3, sort='new')
    operatingsystem_hot = Books.objects.get_books_by_type(OPERATINGSYSTEM, 4, sort='hot')
    database_new = Books.objects.get_books_by_type(DATABASE, 3, sort='new')
    database_hot = Books.objects.get_books_by_type(DATABASE, 4, sort='hot')

    context = {
        'python_new': python_new,
        'python_hot': python_hot,
        'javascript_new': javascript_new,
        'javascript_hot': javascript_hot,
        'algorithms_new': algorithms_new,
        'algorithms_hot': algorithms_hot,
        'machinelearning_new': machinelearning_new,
        'machinelearning_hot': machinelearning_hot,
        'operatingsystem_new': operatingsystem_new,
        'operatingsystem_hot': operatingsystem_hot,
        'database_new': database_new,
        'database_hot': database_hot,
    }

    return render(request, 'books/index.html', context=context)


def detail(request, books_id):
    books = Books.objects.get_books_by_id(books_id=books_id)

    if books is None:
        return redirect(reverse('books:index'))

    books_li = Books.objects.get_books_by_type(type_id=books.type_id, limit=2, sort='new')
    type_title = BOOKS_TYPE[books.type_id]
    context = {'books': books, 'books_li': books_li, 'type_title': type_title}
    return render(request, 'books/detail.html', context)


def list(request, type_id, page):
    # ??????????????????
    sort = request.GET.get('sort', 'default')

    # ??????type_id????????????
    if int(type_id) not in BOOKS_TYPE.keys():
        return redirect(reverse('books:index'))

    # ??????????????????id???????????????????????????
    books_li = Books.objects.get_books_by_type(type_id=type_id, sort=sort)

    # ??????
    paginator = Paginator(books_li, 1)

    # ??????????????????????????????
    num_pages = paginator.num_pages

    # ??????page?????????
    if page == '' or int(page) > num_pages:
        page = 1
    else:
        page = int(page)

    # ??????????????????Page??????????????????
    books_li = paginator.page(page)

    # ??????????????????
    # 1. ?????????<5?????????????????????
    # 2. ???????????????3????????????1-5???
    # 3. ???????????????3???????????????5???
    # 4. ?????????????????????????????????2?????????2???????????????
    if num_pages < 5:
        pages = range(1, num_pages + 1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages - 4, num_pages + 1)
    else:
        pages = range(page - 2, page + 3)

    # ????????????
    books_new = Books.objects.get_books_by_type(type_id=type_id, limit=2, sort='new')

    # ???????????????
    type_title = BOOKS_TYPE[int(type_id)]
    context = {
        'books_li': books_li,
        'books_new': books_new,
        'type_id': type_id,
        'sort': sort,
        'type_title': type_title,
        'pages': pages
    }

    return render(request, 'books/list.html', context)
