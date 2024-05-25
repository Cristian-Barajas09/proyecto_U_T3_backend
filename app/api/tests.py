import unittest
from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.

class ExampleViewTest(TestCase):
    """Example View Test"""
    @unittest.skip("Example View Test")
    def test_example_view(self):
        """Test Example View."""
        client = APIClient()
        response = client.get('/api/v1/example/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, World!','example':None})

    @unittest.skip("Example View Test with query parameter")
    def test_example_view_with_query_parameter(self):
        """Test Example View with query parameter."""
        client = APIClient()
        response = client.get('/api/v1/example/', {'example': 'example'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, World!', 'example': 'example'})