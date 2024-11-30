from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Фото')
    phone_number = models.CharField(max_length=14, null=True, blank=True)

    class Meta:
        __db_table__ = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


@receiver(post_delete, sender=User)
def delete_user_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

