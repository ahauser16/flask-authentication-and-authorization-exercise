import unittest
from app import app

class RedirectTestCase(unittest.TestCase):
    """ To run the tests, navigate to the root of your project in the terminal and execute: `python -m unittest discover -s tests` """
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_redirect(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/register', response.location)

    def test_flash_message(self):
        with app.test_client() as client:
            response = client.get('/')
            with client.session_transaction() as session:
                flash_messages = session['_flashes']
                self.assertIn(('info', 'You are being redirected to the registration page.'), flash_messages)

if __name__ == '__main__':
    unittest.main()