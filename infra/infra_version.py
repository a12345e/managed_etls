from typing import Final


class InfraVersion:
    def __init__(self):
        self._number: Final[str] = '1.0'
        self._description:  Final[str] = 'initial'

    @property
    def description(self):
        return self._description

    @property
    def number(self):
        return self._number
