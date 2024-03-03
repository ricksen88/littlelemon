from django.test import TestCase

from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)

        title = item.title
        price = item.price

        expected_string = f"{title} : {price}"

        self.assertEqual(expected_string, "IceCream : 80")
