from django.http import HttpResponse, HttpRequest, QueryDict, HttpResponseNotFound, Http404, \
    HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, ]



menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    d = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db}
    return render(request, 'women/index.html', context=d)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html', {'title': 'O saite', 'menu': menu})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"<h1>post with post_id={post_id}</h1>")

def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")