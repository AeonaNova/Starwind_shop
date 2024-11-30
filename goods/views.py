from django.views.generic import ListView, DetailView
from django.http import Http404
from .utils import q_search
from .models import Categories, Goods


class CatalogView(ListView):
    model = Goods
    template_name = 'goods/catalog.html'
    context_object_name = 'product'
    paginate_by = 3
    allow_empty = True
    slug_url_kwarg = 'category_slug' # поступает из urls, с запросом 'request'

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        query = self.request.GET.get('q')
        print(query)

        if category_slug == 'all':
            product = super().get_queryset() #обращение к MultipleObjectMixin классу
        elif query:
            product = q_search(query)
        else:
            product = super().get_queryset().filter(category__slug=category_slug)
            if not product.exists():
                raise Http404()
        if on_sale:
            product = product.filter(discount__gt=0)

        if order_by and order_by != 'default':
            product = product.order_by(order_by)

        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)#обращение к MultipleObjectMixin классу
        context["title"] = 'Starwind'
        context["slug_ulr"] = self.kwargs.get(self.slug_url_kwarg)

        return context


class GoodsView(DetailView):
    template_name = 'goods/product.html'
    context_object_name = 'thing'
    slug_url_kwarg = 'product_slug'

    def get_object(self, query_set=None):
        product = Goods.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


# def goods(request, product_slug=None):
#     thing = Goods.objects.get(slug=product_slug)
#
#     context = {'thing': thing}
#
#     return render(request, 'goods/product.html', context)

# def catalog(request, category_slug=None):
#
#     query = request.GET.get('q', 1)
#
#     if category_slug == 'all':
#         categories = Categories.objects.all()
#         product = Goods.objects.all()
#
#     else:
#         # categories = Categories.objects.filter(slug=category_slug)
#         product = Goods.objects.filter(category__slug=category_slug)
#     paginator = Paginator(product, 3)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.page(int(page_number)) #get_page
#
#     context = {
#         "title": 'Товары раздела ' ,#+ categories[0].name
#         # "categories": categories,
#         "slug_url": category_slug,
#         "product": page_obj
#     }
#     return render(request, 'goods/catalog.html', context)


