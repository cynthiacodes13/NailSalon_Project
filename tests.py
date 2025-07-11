import unittest
from server import app
from model import connect_to_db, db


class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Something that does before every test"""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
    
    def test_homepage(self):
        """Test the homepage"""

        result = self.client.get("/")
        self.assertIn(b"Welcome",result.data)


    def test_signin(self):
        """Test the sign in page"""

        result = self.client.post("/signin", data={"username": "cindy", "password": "123"},
                                  follow_redirects=True)
        self.assertIn(b"We care for our users", result.data)


    def test_appointment_form(self):
        """Test the appointment form"""

        result = self.client.post("/appointment", data={"data":"04/10/24", "time": "10:00am", "manitype":"Gel Manicure", 
                                                        "manishape":"Coffin", "manicolor":"Green", "pedi": "Yes", "pedicolor":"Green"})
        self.assertIn(b'Super Cool! We are getting the same Manicure and Pedicure', result.data)
        
        


if __name__ == "__main__":
    unittest.main()
