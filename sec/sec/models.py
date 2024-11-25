from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название')
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='URl')
    description = models.TextField(blank=True, unique=True, null=True, verbose_name='описание')
    timecreation = models.DateTimeField(auto_created=True, verbose_name='время добавления')
    image = models.ImageField(upload_to='goods_images', null=True, blank=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default='0.00', max_digits=4, decimal_places=2, verbose_name= 'скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='категории')



    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Categories(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True, blank=True, verbose_name='Категория')
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='URl')


