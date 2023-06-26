from django.test import TestCase
from .models import Customer

# Create your tests here.


class CustomerModelTest(TestCase):

    def setUpTestData():
        Customer.objects.create(
            name='Test Customer', notes='This is our first test customer', pic='no_image.jpg')

    def test_customer_name(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
