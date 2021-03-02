from django.test import TestCase
from django.urls import reverse # a importer

# Create your tests here.

class IndexPageTestCase(TestCase):
    def test_index_page(self):
        #self.assertEqual('a', 'a')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
