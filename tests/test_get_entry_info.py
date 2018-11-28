import unittest
import json
import os

from unittest.mock import MagicMock
from swc_registry.get_entry_info import SWC
from swc_registry.get_entry_info import SWCRegistry


class TestMethods(unittest.TestCase):
    def setUp(self):
        with open(
            os.path.dirname(__file__) + "/../swc_registry/swc-.json"
        ) as f:
            self.object = json.load(f)
        self.swc = SWC("SWC-100")
        SWCRegistry()._load_from_file()

    def test_get_title(self):
        self.assertEqual(self.swc.title, self.object["SWC-100"]["content"]["Title"])

    def test_get_relationships(self):
        self.assertEqual(
            self.swc.relationships, self.object["SWC-100"]["content"]["Relationships"]
        )

    def test_get_description(self):
        self.assertEqual(
            self.swc.description, self.object["SWC-100"]["content"]["Description"]
        )

    def test_get_remediation(self):
        self.assertEqual(
            self.swc.remediation, self.object["SWC-100"]["content"]["Remediation"]
        )

    def test_get_last_version(self):
        # Act
        after_content = SWCRegistry().content
        after_content["SWC-100"]["content"]["Title"] = "Brick"
        SWCRegistry._get_latest_version = MagicMock(return_value=after_content)

        SWCRegistry().update()

        # Assert
        new_title = self.swc.title
        self.assertEqual(new_title, "Brick")


if __name__ == "__main__":
    unittest.main()
