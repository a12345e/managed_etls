from abc import ABC
import string
from typing import Sequence
from infra.abstracts.operator.etl import Etl
from infra.abstracts.operator.sensor import Sensor
from infra.realm import Realm


class Principal(ABC):
    """
      The Principal is actually the manager defining the goals of a shift run.
      The current configuration applied by the Principal are:
        - list of sensors,
        - list of etls
        - realm

    """
    def __int__(self,
                name: string,
                realm: Realm,
                etls: Sequence[Etl],
                sensors: Sequence[Sensor]):
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