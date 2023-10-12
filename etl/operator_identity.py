import string
from typing import Final
from enum import Enum, auto


class OperatorIdentity:
    class Type(Enum):
        Sensor = auto()
        ETL = auto()

    def __init__(self,
                 operator_type: Type,
                 name: string,
                 version_number: string,
                 version_description: string):
        self._operator_type: Final[OperatorIdentity.Type] = operator_type
        self._name: Final[string] = name
        self._version_number: Final[string] = version_number
        self._version_description:  Final[string] = version_description

    @property
    def operator_type(self):
        return self._operator_type

    @property
    def name(self):
        return self._name

    @property
    def version_description(self):
        return self._version_description

    @property
    def version_number(self):
        return self._version_number
