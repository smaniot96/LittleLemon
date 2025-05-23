from django.test import TestCase
from reservation.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Test Item", price=2, inventory=10)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Test Item : 2 : 10")