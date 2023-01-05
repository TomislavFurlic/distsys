import unittest
import json
import mysql.connector
from app import app

class TestFakeEUcenjeAPI(unittest.TestCase):
    def setUp(self):
        # Create a test client for the app
        self.client = app.test_client()
        # Database
        conn = mysql.connector.connect(
            user="tfurlic",
            password="tomislavfurlic",
            host="db4free.net",
            database="unipu2023"
        )
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE repos")
        conn.commit()
        cursor.execute("INSERT INTO repos (username, ghlink, filename) VALUES ('user1', 'https://github.com/user1/repo1', 'repo1')")
        cursor.execute("INSERT INTO repos (username, ghlink, filename) VALUES ('user2', 'https://github.com/user2/repo2', 'repo2')")
        cursor.execute("INSERT INTO repos (username, ghlink, filename) VALUES ('user3', 'https://github.com/user3/repo3', 'repo3')")
        conn.commit()

    def test_get_links(self):
        # Send a GET request to the route
        response = self.client.get('/get_links')
        # Get the response data as a dictionary
        data = json.loads(response.data)
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the lists in the response data have the expected lengths
        self.assertEqual(len(data['usernames']), 3)
        self.assertEqual(len(data['githubLinks']), 3)
        self.assertEqual(len(data['filename']), 3)
        # Assert that the lists in the response data have the expected values
        self.assertEqual(data['usernames'], ['user1', 'user2', 'user3'])
        self.assertEqual(data['githubLinks'], ['https://github.com/user1/repo1', 'https://github.com/user2/repo2', 'https://github.com/user3/repo3'])
        self.assertEqual(data['filename'], ['repo1', 'repo2', 'repo3'])
    
    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute("TRUNCATE TABLE repos")
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()