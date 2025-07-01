import unittest
from server import app
from model import connect_to_db, db


class FlaskTests(unittest.TestCase):

    def setUp(self):

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
    
    def test_homepage(self):

        result = self.client.get("/")
        self.assertIn(b"Welcome",result.data)


    def test_signin(self):


if __name__ == "__main__":
    unittest.main()
