from django.views.generic import ListView, DetailView
from django.http import Http404
from .utils import q_search
from .models import Goods


class CatalogView(ListView):
    model = Goods
    template_name = 'goods/catalog.html'
    context_object_name = 'product'
    paginate_by = 3
    allow_empty = True
    slug_url_kwarg = 'category_slug'  # поступает из urls, с запросом 'request'

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        query = self.request.GET.get('q')

        if category_slug == 'all':
            product = super().get_queryset()  # обращение к MultipleObjectMixin классу
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
        context = super().get_context_data(**kwargs)  # обращение к MultipleObjectMixin классу
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
