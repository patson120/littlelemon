

from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse


class MenuViewTestCase(TestCase):

    def setUp(self):
        menu = Menu.objects.create(title='IceCream', price=80)

    def test_get_all(self):
        response = self.client.get(reverse('restaurant:menu_items'))
        self.assertEqual(response.status_code, 200)