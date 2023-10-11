import string
from typing import Final


class OperatorIdentity:
    def __init__(self, name: string,
                 version_number: string,
                 version_description: string):
        self._name: Final[string] = name
        self._version_number: Final[string] = version_number
        self._version_description:  Final[string] = version_description

    @property
    def name(self):
        return self._name

    @property
    def version_description(self):
        return self._version_description

    @property
    def version_number(self):
        return self._version_number
