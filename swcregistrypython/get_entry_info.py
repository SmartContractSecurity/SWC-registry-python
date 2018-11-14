import urllib.request
import json


class SWC:
    def __init__(self, swc_id):
        self.swc_id = swc_id

    def get_last_version(self):
        url = ('https://raw.githubusercontent.com/SmartContractSecurity/SWC-registry/master/export/swc-definition.json')
        response = urllib.request.urlopen(url)
        converted_response = response.read()
        decoded_response_info = converted_response.decode(response.info().get_param('charset') or 'utf-8')
        response = json.loads(decoded_response_info)
        return response

    def get_content(self):
        entries = self.get_last_version()
        current_entry = entries.get(self.swc_id, {})
        content = current_entry.get('content', {})
        return content

    def get_title(self):
        content = self.get_content()
        title = content.get('Title', {})
        return title

    def get_relationships(self):
        content = self.get_content()
        relationships = content.get('Relationships', {})
        return relationships

    def get_description(self):
        content = self.get_content()
        description = content.get('Description', {})
        return description

    def get_remediation(self):
        content = self.get_content()
        remediation = content.get('Remediation', {})
        return remediation
