from datetime import datetime
from uuid import uuid4
from typing import List, final
from enum import Enum
from data_cntrl.data_classes.model.product import Product
from typing import Final
from component_id.abstract.component_id import ComponentId
from component_id.managed_operations_version.managed_operations_version import managed_operations_version


@final
class Operation:
    class PHASE(Enum):
        CREATE = 1
        READY = 2
        FAILED = 3
        IGNORED = 4
        USED = 5

    def __init__(self,
                 principal: str,
                 mission: Product,
                 create_time: datetime,
                 using_operations: List[str],
                 used_by_operations: List[str] = []):

        """
        Operation adds the context of principal, and process to a mission being materialized
        :param principal: the name of the principal doing this operation
        :param mission: the mission product
        :param create_time: the time of creation
        :param using_operations: operation ids
        :param used_by_operations: operation ids
        """
        self._principal: Final[str] = principal
        self._mission: Final[Product] = mission
        self._create_time: Final[datetime] = create_time
        self._phase = Operation.PHASE.CREATE
        self._using_operations = using_operations
        self._used_by_operations = used_by_operations
        self._complete_create_time = None
        self._complete_usage_time = None
        self._id = uuid4()

    @property
    def id(self):
        return self._id

    @property
    def principal(self):
        return self._principal

    @property
    def mission(self):
        return self._mission

    @property
    def create_time(self):
        return self._create_time

    @property
    def complete_usage_time(self):
        return self._complete_usage_time

    @property
    def complete_create_time(self):
        return self._complete_create_time

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, phase: PHASE):
        if self._phase.value >= phase.value:
            raise Exception("Set phase to " + phase.name + " while already phase is " + self._phase.name)
        if self._phase != Operation.PHASE.READY and phase == Operation.PHASE.USED:
            raise Exception("Set phase to " + phase.name + " while yet phase is " + self._phase.name)
        if phase == Operation.PHASE.USED:
            self._complete_usage_time = datetime.now()
        else:
            self._complete_create_time = datetime.now()
