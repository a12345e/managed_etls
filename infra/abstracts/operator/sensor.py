import datetime
import string
from abc import abstractmethod
from typing import Sequence
from abc import ABC
from infra.operator import Operator
from infra.operation import Operation
from infra.abstracts.mng.principal import Principal


class Sensor(ABC, Operator):
    """
    Sensors are used to discover raw materials (operations) prepared by our suppliers.
    Unlike our ETL the operator of discovery
    creates an operator that has no source operations as those source operations creating the raw materials
    come from our suppliers realm.
    Sensors can run in context of an OperationsManager or can run from a one time impl, doing one time shot.
    """

    def __init__(self, name: string,
                 version_number: string,
                 version_description: string):
        super().__init__(name, version_number, version_description)

    @abstractmethod
    def discover(self, principal: Principal, start_time: datetime = None, end_time: datetime.datetime = None) \
            -> Sequence[Operation]:
        pass
