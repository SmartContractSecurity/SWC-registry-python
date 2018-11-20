import os
import requests
import json


class SWC:
    def __init__(self, swc_id):
        self.swc_id = swc_id
        self.path_file_content = os.path.join(os.path.dirname(__file__),'swc-definition.json')

    @property
    def get_content_by_file(self):
        with open(self.path_file_content, 'r') as f:
            response = json.load(f)
        return response

    @property
    def get_last_version(self):
        try:
            url = ('https://raw.githubusercontent.com/SmartContractSecurity/SWC-registry/master/export/swc-definition.json')
            response = requests.get(url).json()
            with open(self.path_file_content, 'w') as outputfile:
                json.dump(response, outputfile)
        except requests.exceptions.RequestException:
            response = self.get_content_by_file
        return "swc-definition.json - updated"

    @property
    def content(self):
        entries = self.get_content_by_file
        current_entry = entries.get(self.swc_id, {})
        content = current_entry.get('content', {})
        return content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def title(self):
        content = self.content
        title = content.get('Title', {})
        return title

    @property
    def relationships(self):
        content = self.content
        relationships = content.get('Relationships', {})
        return relationships

    @property
    def description(self):
        content = self.content
        description = content.get('Description', {})
        return description

    @property
    def remediation(self):
        content = self.content
        remediation = content.get('Remediation', {})
        return remediation
