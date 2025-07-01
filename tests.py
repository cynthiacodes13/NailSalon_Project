import unittest
import server

class FlaskTests(unittest.TestCase):

    def setUp(self):

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
    
    def test_homepage(self):

        result = self.client.get("/")
        self.assertIn(b"Welcome",result.data)



if __name__ == "__main__":
    unittest.main()
