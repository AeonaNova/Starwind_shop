import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sec.sec.settings')
os.environ.setdefault('DJANGO_ROOT_URLCONF', 'sec.sec.urls')# для запуска тестов и локально
django.setup()

from django.test import TestCase
from django.urls import reverse
from goods.models import Goods

class MyTest(TestCase):
    def setUp(self):
        Goods.objects.create(
            name="Test good",
            description="Test Description",
            timecreation="2024-08-01 17:06:05.299371+03",
            category_id=6
        )

    def test_urlstesting(self):
        url = reverse('main:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def db_test(self):
        goods = Goods.objects.all()
        check_goods = {
        'name' : "Test good",
        'description' : "Test Description",
        'timecreation' : "2024-08-01 17:06:05.299371+03",
        'category_id' : 6
        }
        self.assertEqual(goods, check_goods)
