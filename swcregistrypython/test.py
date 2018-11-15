import unittest
import json

from unittest.mock import MagicMock
from get_entry_info import SWC


class TestMethods(unittest.TestCase):
    def setUp(self):
        with open('swc-definition.json') as f:
            self.object = json.load(f)
        self.swc = SWC('SWC-100')
        self.dd = {
                        "Title": "Function Default Visibility",
                        "Relationships": "[CWE-710: Improper Adherence to Coding Standards](https://cwe.mitre.org/data/definitions/710.html)",
                        "Description": "Functions that do not have a function visibility type specified are `public` by default. This can lead to a vulnerability if a developer forgot to set the visibility and a malicious user is able to make unauthorized or unintended state changes.",
                        "Remediation": "Functions can be specified as being `external`, `public`, `internal` or `private`. It is recommended to make a conscious decision on which visibility type is appropriate for a function. This can dramatically reduce the attack surface of a contract system."
                      }
     
    def test_get_title(self):
        self.swc.get_content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.get_title(), self.object['SWC-100']['content']['Title'])

    def test_get_relationships(self):
        self.swc.get_content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.get_relationships(), self.object['SWC-100']['content']['Relationships'])

    def test_get_description(self):
        self.swc.get_content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.get_description(), self.object['SWC-100']['content']['Description'])
    
    def test_get_remediation(self):
        self.swc.get_content = MagicMock(return_value=self.object['SWC-100']['content'])
        self.assertEqual(self.swc.get_remediation(), self.object['SWC-100']['content']['Remediation'])

        
if __name__ == '__main__':
    unittest.main()