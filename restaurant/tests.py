from django.test import TestCase
from django.urls import reverse

from . import models, views

# Create your tests here.
class MenuItemTestCase(TestCase):

    def test_get_items(self):
        item = models.MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_items()
        self.assertEqual(itemstr, "IceCream : 80")

class MenuTest(TestCase):

    def test_get_item(self):
        menu = models.Menu.objects.create(title='IceCream', price=80)
        self.assertEqual(menu.__str__(), "IceCream : 80")


class MenuViewTestCase(TestCase):

    def setUp(self):
        menu = models.Menu.objects.create(title='IceCream', price=80)

    def test_get_all(self):
        response = self.client.get(reverse('restaurant:menu_items'))
        self.assertEqual(response.status_code, 200)