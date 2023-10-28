import datetime
from abc import abstractmethod
from typing import Sequence
from abc import ABC
from component_id.abstract.component_id import ComponentId
from data_cntrl.data_classes.model import Operation
from application.abstract.application import Context


class Sensor(ABC):
    """
    Sensors are used to discover raw materials (operations) prepared by our suppliers.
    Unlike our Etl the operators of discovery
    creates an operators that has no source operations as those source operations creating the raw materials
    come from our suppliers realm.
    Sensors can run in context of an OperationsManager or can run from a one time managed_operations_version, doing one time shot.
    """

    def __init__(self, id: ComponentId):
        self._id = id

    @abstractmethod
    def discover(self, principal: Context, start_time: datetime = None, end_time: datetime.datetime = None) \
            -> Sequence[Operation]:
        pass
