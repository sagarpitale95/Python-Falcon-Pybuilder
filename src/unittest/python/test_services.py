"""
Unit tests for services
"""
from falcon import testing

from src.main.python.app import api


class TestHelloWorldService(testing.TestCase):

    def setUp(self):
        self.api = testing.TestClient(api)

    def test_hello_world(self):
        resp = self.api.simulate_get('/hi')
        self.assertDictEqual(resp.json, {'greeting': 'Hi!'})
