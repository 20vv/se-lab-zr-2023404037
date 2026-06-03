import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)
    
    def test_status_endpoint(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'running')
        self.assertEqual(data['message'], 'CI/CD pipeline is working!')
    
    def test_greet_endpoint(self):
        response = self.app.get('/api/greet/Alice')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Hello, Alice!')
        self.assertEqual(data['status'], 'success')
    
    def test_invalid_endpoint(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
