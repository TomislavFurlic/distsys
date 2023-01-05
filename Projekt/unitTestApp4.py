import unittest
import time
import os
from app4 import app

class TestFourthMicroservice(unittest.TestCase):
    def setUp(self):
        # Create a test client for the app
        self.client = app.test_client()
        # Set the base URL for the endpoint
        self.url = '/gather_data'

    def test_gather_data(self):
        # Set the data to be passed in the request
        data = ['username1', 'username2', 'username3', 'username4', 'username5',
                'username6', 'username7', 'username8', 'username9', 'username10',
                'username11']
        # Make a POST request to the endpoint with the data
        response = self.client.post(self.url, json=data)
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Give the asynchronous tasks enough time to complete
        time.sleep(1)
        # Check that the files were created and contain the correct data
        for i, element in enumerate(data):
            with open(f"file{i}.txt") as f:
                self.assertEqual(f.read(), element)
        # Delete the created files
        for i in range(len(data)):
            os.remove(f"file{i}.txt")

if __name__ == '__main__':
    unittest.main()