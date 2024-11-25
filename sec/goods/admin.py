from django.contrib import admin

from goods.models import Goods, Categories


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')  # Выводимые поля в админке

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Categories, CategoriesAdmin)