from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.CatalogView.as_view(), name='search'),
     path('<slug:category_slug>/', views.CatalogView.as_view(), name='index'),
    # path('<slug:category_slug>/', views.catalog, name='index'),
    # path('product/<slug:product_slug>/', views.goods, name='product'),
    path('product/<slug:product_slug>/', views.GoodsView.as_view(), name='product'),

]

