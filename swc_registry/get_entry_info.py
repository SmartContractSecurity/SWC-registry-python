import os
import requests
import json


class SWCException(Exception):
    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SWCRegistry(object, metaclass=Singleton):
    """
    Registry class takes care of loading and downloading the swc registry
    """

    def __init__(self):
        self._content = None

    @staticmethod
    def _get_latest_version():
        try:
            url = (
                "https://raw.githubusercontent.com/SmartContractSecurity/SWC-registry/master/export/swc-definition"
                ".json"
            )
            response = requests.get(url).json()
            return response
        except requests.exceptions.RequestException:
            return None

    def _load_from_file(self):
        path_file_content = os.path.join(
            os.path.dirname(__file__), "swc-definition.json"
        )
        with open(path_file_content, "r") as f:
            self._content = json.load(f)

    def update(self):
        self._content = SWCRegistry._get_latest_version()

    @property
    def content(self):
        if self._content is None:
            self._load_from_file()
        return self._content

    def __repr__(self):
        return "<SWCRegistry with {} entries>".format(len(self.content.keys()))


class SWC:
    """
    SWC class contains information on an SWC entry

    Example usage:
        swc = SWC('SWC-100')
        print(swc.title)
    """

    def __init__(self, swc_id, get_last=False):
        self.swc_id = swc_id
        if get_last:
            SWCRegistry().update()

    @property
    def _swc_content(self):
        return SWCRegistry().content

    @property
    def _content(self):
        entries = self._swc_content
        current_entry = entries.get(self.swc_id)
        if not current_entry:
            raise SWCException("SWC with ID {} does not exist".format(self.swc_id))
        content = current_entry.get("content", {})
        return content

    @property
    def title(self) -> str:
        content = self._content
        title = content.get("Title", "")
        return title

    @property
    def relationships(self) -> str:
        content = self._content
        relationships = content.get("Relationships", "")
        return relationships

    @property
    def description(self) -> str:
        content = self._content
        description = content.get("Description", "")
        return description

    @property
    def remediation(self) -> str:
        content = self._content
        remediation = content.get("Remediation", "")
        return remediation

    def __repr__(self):
        return "<SWC swc_id={0.swc_id} title={0.title}>".format(self)
