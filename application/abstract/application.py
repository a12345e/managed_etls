import pydantic
from typing import List


class Context(pydantic.BaseModel):
    """
    Realm is about the data plane physical state. The specific data_cntrl/databases we are using
    in our operation
    """
    def __init__(self, name: str, realm: str, etls: List[str], sensors: List[str]):
        self._name = name
        self._realm = realm
        self._etls = etls
        self._sensors = sensors

    @property
    def name(self):
        return self._name

    @property
    def realm(self):
        return self._realm

    @property
    def etls(self):
        return self._etls

    @property
    def sensors(self):
        return self._sensors

