import datetime
import string
from abc import abstractmethod
from typing import Sequence
from abc import ABC
from infra.product import Product
from infra.operation import Operation
from infra.operator import Operator
from infra.principal import Principal


class Sensor(ABC, Operator):
    """
    Sensors are used to discover raw materials (operations) prepared by our suppliers.
    Unlike our ETL the operation of discovery
    creates an operation that has no source operations as those source operations creating the raw materials
    come from our suppliers realm.
    Sensors can run in context of an OperationsManager or can run from a one time application, doing one time shot.
    """
    def __init__(self, name: string,
                 version_number: string,
                 version_description: string):
        super().__init__(name, version_number, version_description)

    @abstractmethod
    def discover(self, principal: Principal, start_time: datetime, end_time: datetime.datetime) -> Operation:
        pass

    @abstractmethod
    def discover(self, principal: Principal, partitions: Sequence[string]) -> Operation:
        pass
