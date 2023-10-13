from datetime import datetime
from typing import final
from manager.principal import Principal
from product import Product
from typing import Final


@final
class Operation:
    def __init__(self,
                 principal: Principal,
                 mission: Product,
                 create_time: datetime):
        """
        So what about operation that not exist in product: Operation adds the context of principal, time events and
        other eventualities that will be defined later. Operation is about principal and process history details
        :param principal:
        :param mission:
        :param create_time:
        """
        self._principal: Final[Principal] = principal
        self._mission: Final[Product] = mission
        self._create_time: Final[datetime] = create_time
        self._ready_time = None
        self._complete_usage_time = None

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
    def ready_time(self):
        return self._ready_time

    @property
    def complete_usage_time(self):
        return self._complete_usage_time

    @property.setter
    def ready_time(self, ready_time: datetime):
        self._ready_time = ready_time

    @property.setter
    def complete_usage_time(self, complete_usage_time: datetime):
        self._complete_usage_time = complete_usage_time

