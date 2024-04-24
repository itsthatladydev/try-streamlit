import unittest
from server import app

class TestPredict(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict_success(self):
        response = self.app.get('/predict?airport_id=123&day_of_week=1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('model_prediction', data)
        self.assertIn('confidence_percent', data)
        self.assertIn('delayed_percent', data)
        self.assertIn('interpretation', data)

    def test_predict_invalid_input(self):
        response = self.app.get('/predict?airport_id=abc&day_of_week=xyz')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()