from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product

class ProductViewTests(TestCase):
    def setUp(self):
        self.client = Client() #Setting up default Client

        #Define Default Product to test
        self.Product = Product.objects.create(name = 'test Product', price='10.0') #required fields must be given here

    def test_form_submit(self):

        # variable = self.client.post(reverse('URLNAME', {'field_name':'FieldValue','field_name':'FieldValue',........ }))
        response = self.client.post(reverse('product'), {'name': 'test Product', 'price': '10.0'})

        # assertEquala()  Checks the variable status code : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        self.assertEqual(response.status_code, 200)
    
    def test_edit_product(self):
        # variable = self.client.post(reverse('URLNAME', {'edit':self.Model.ID, 'field_name':'FieldValue','field_name':'FieldValue',........ }))
        response = self.client.post(reverse('product'), {'edit': self.Product.id, 'name': 'Edit Test Product', 'price': '20.0'})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_product(self):
        # variable = self.client.post(reverse('URLNAME', {'delete': self.Model.id, 'field_name':'FieldValue','field_name':'FieldValue',........ }))
        response = self.client.post(reverse('product'), {'delete':self.Product.id})
        self.assertEqual(response.status_code, 200)