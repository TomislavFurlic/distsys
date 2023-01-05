import unittest
import json
from app2 import app

class TestFirstMicroservice(unittest.TestCase):
    def setUp(self):
        # Create a test client for the app
        self.client = app.test_client()
        # Set the base URL for the endpoint
        self.url = '/call_elearning_api'
    
    def test_call_elearning_api(self):
        # Make a POST request to the endpoint
        response = self.client.post(self.url)
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response data is correct
        self.assertEqual(response.data, b'E-learning API called and data passed to the 2nd microservice!')

if __name__ == '__main__':
    unittest.main()