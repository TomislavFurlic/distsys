import unittest
import json
from app3 import app

class TestSecondMicroservice(unittest.TestCase):
    def setUp(self):
        # Create a test client for the app
        self.client = app.test_client()
        # Set the base URLs for the endpoints
        self.url_wt_w = '/wt_w'
        self.url_wt_d = '/wt_d'

    def test_wt_w(self):
        # Set the data to be passed in the request
        data = ['username1', 'username2', 'username3', 'username4', 'username5',
                'username6', 'username7', 'username8', 'username9', 'username10',
                'username11']
        # POST request to the endpoint with the data
        response = self.client.post(self.url_wt_w, json=data)
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response data is correct
        self.assertEqual(response.data, b'Data filtered and passed to 4th microservice!')

    def test_wt_d(self):
        # Set the data to be passed in the request
        data = ['username1', 'username2', 'username3', 'username4', 'username5',
                'username6', 'username7', 'username8', 'username9', 'username10',
                'username11']
        # POST request to the endpoint with the data
        response = self.client.post(self.url_wt_d, json=data)
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response data is correct
        self.assertEqual(response.data, b'Data filtered and passed to 4th microservice!')

if __name__ == '__main__':
    unittest.main()