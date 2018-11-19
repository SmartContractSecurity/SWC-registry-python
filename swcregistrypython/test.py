import unittest
import json

from unittest.mock import MagicMock
from get_entry_info import SWC


class TestMethods(unittest.TestCase):
    def setUp(self):
        with open('swc-definition.json') as f:
            self.object = json.load(f)
        self.swc = SWC('SWC-100')
     
    def test_get_title(self):
        self.swc.content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.title, self.object['SWC-100']['content']['Title'])

    def test_get_relationships(self):
        self.swc.content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.relationships, self.object['SWC-100']['content']['Relationships'])

    def test_get_description(self):
        self.swc.content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.description, self.object['SWC-100']['content']['Description'])
    
    def test_get_remediation(self):
        self.swc.content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.remediation, self.object['SWC-100']['content']['Remediation'])

    def test_get_last_version(self):
        self.object['SWC-100']['content']['Title'] = "Test"
        with open('swc-definition.json', 'w') as f:
            json.dump(self.object, f)
        self.assertEqual(self.swc.title, "Test")
        
        self.swc.get_last_version
        self.assertNotEqual(self.swc.title, "Test")


if __name__ == '__main__':
    unittest.main()