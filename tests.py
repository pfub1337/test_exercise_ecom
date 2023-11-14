import json
import unittest

from main import app, db


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.data = self.load_test_data("tests.json")
    

    def load_test_data(self, filename):
        with open(filename, "r") as f:
            return json.load(f)
    

    def test_correct_get_form(self):
        print(f"\n{'-'*20}\nCorrect data:\n")
        for rec in self.data["correct"]:
            response = self.app.post('/get_form', data=rec)
            print(response.data)
            assert response.status_code == 200
    
    def test_incorrect_get_form(self):
        print(f"\n{'-'*20}\nIncorrect data:\n")
        for rec in self.data["incorrect"]:
            response = self.app.post('/get_form', data=rec)
            print(response.data)


if __name__ == "__main__":
    unittest.main()
