from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    return render(request, 'main/index.html', {'title': 'Магазин Starwind', 'categories': categories})


def about(request):
    return render(request, 'main/about.html', {'title': 'Страница о том почему компания такая уникальная и товар такой классный'})
