import urllib.request
import json


class SWC:
    def __init__(self, swc_id):
        self.swc_id = swc_id
        self.path_file_content = 'swc-definition.json'

    def get_content_by_file(self):
        with open(self.path_file_content, 'r') as f:
            response = json.load(f)
        return response

    def get_last_version(self):
        try:
            url = ('https://raw.githubusercontent.com/SmartContractSecurity/SWC-registry/master/export/swc-definition.json')
            response = urllib.request.urlopen(url)
            converted_response = response.read()
            decoded_response_info = converted_response.decode(response.info().get_param('charset') or 'utf-8')
            response = json.loads(decoded_response_info)
            with open(self.path_file_content, 'w') as outputfile:
                json.dump(data, outputfile)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            response = self.get_content_by_file()
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
