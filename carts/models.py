from django.db import models


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to='users.User', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to='goods.Goods', on_delete=models.CASCADE, verbose_name='Товар')
    creation_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ("id",)

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.final_price() * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.user} | Товар {self.product.name} | Количество {self.quantity}'
