import urllib.request
import json


class SWC:
    def __init__(self, swc_id):
        self.swc_id = swc_id

    def get_last_version(self):
        url = ('https://raw.githubusercontent.com/SmartContractSecurity/SWC-registry/master/export/swc-definition.json')
        r = urllib.request.urlopen(url)
        response = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
        return response

    def get_title(self):
        entries = self.get_last_version()
        return entries[self.swc_id]['content']['Title']

    def get_relationships(self):
        entries = self.get_last_version()
        return entries[self.swc_id]['content']['Relationships']

    def get_description(self):
        entries = self.get_last_version()
        return entries[self.swc_id]['content']['Description']

    def get_remediation(self):
        entries = self.get_last_version()
        return entries[self.swc_id]['content']['Remediation']
