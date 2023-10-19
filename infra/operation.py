from datetime import datetime
from uuid import uuid4
from typing import Sequence, final
from enum import Enum
from infra.principal import Principal
from infra.product import Product
from typing import Final


@final
class Operation:
    class PHASE(Enum):
        CREATE = 1
        READY = 2
        FAILED = 3
        IGNORED = 4
        USED = 5

    def __init__(self,
                 principal: Principal,
                 mission: Product,
                 create_time: datetime,
                 using_operations: Sequence[str] = Sequence[str],
                 used_by_operations: Sequence[str] = Sequence[str]):

        """
        Operation adds the context of principal, and process to a mission being materialized
        :param principal:
        :param mission:
        :param create_time:
        :param using_operations:
        :param used_by_operations:
        """
        self._principal: Final[Principal] = principal
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
