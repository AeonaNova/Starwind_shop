from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.


def index(request):
    categories = Categories.objects.all()
    # context = {
    #     'id': 'Home',
    #     'content' : 'Главная страница магазина - Home'
    # }
    return render(request, 'main/index.html', {'title': 'Магазин Starwind', 'categories': categories})
# render, 'index.html'


def about(request):
    return render(request, 'main/about.html', {'title': 'Страница о том почему компания такая уникальная и товар такой классный'})
