import unittest
from fastapi.testclient import TestClient
from research.api import app
class ApiTests(unittest.TestCase):
 def test_health(self):
  with TestClient(app) as client:
   self.assertEqual(client.get('/health').json()['implementation'],'research_baseline')
 def test_unknown_payload_rejected(self):
  with TestClient(app) as client:
   self.assertEqual(client.post('/v1/baseline',json={'unexpected':'field'}).status_code,422)
 def test_valid_baseline(self):
  with TestClient(app) as client:
   response=client.post('/v1/baseline',json={'candidates': [{'id': 'A', 'position': 'P', 'cost': 8, 'mean': 4, 'variance': 1}], 'budget': 8, 'requirements': {'P': 1}})
   self.assertEqual(response.status_code,200)
   self.assertEqual(response.json()['result'],{'ids': ['A'], 'cost': 8.0, 'expected_performance': 4.0, 'variance': 1.0, 'objective': 4.0, 'assumption': 'independent candidate outcomes'})
