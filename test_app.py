import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    # Test if the home route works
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Test if the scrape route works
    def test_scrape(self):
        tester = app.test_client(self)
        response = tester.post('/scrape', json={"url": "https://www.example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.json)
        self.assertIn('sentiment', response.json)

if __name__ == '__main__':
    unittest.main()
