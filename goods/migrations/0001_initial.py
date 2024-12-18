# Generated by Django 4.2.13 on 2024-08-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Категория')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='URl')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecreation', models.DateTimeField(auto_created=True, verbose_name='время добавления')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='URl')),
                ('description', models.TextField(blank=True, null=True, unique=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default='0.00', max_digits=4, verbose_name='скидка')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.categories', verbose_name='категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
