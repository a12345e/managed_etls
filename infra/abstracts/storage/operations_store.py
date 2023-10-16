from abc import ABC, abstractmethod
from typing import Sequence, Callable
import string
from datetime import datetime
from infra.operation import Operation


class OperationsStore(ABC):

    @abstractmethod
    def get_operations(self, filter: Callable) -> Sequence[Operation]:
        pass

    @abstractmethod
    def create_operations(self, operations: Sequence[Operation]):
        pass

    @abstractmethod
    def update_operations(self, operations: Sequence[Operation]):
        pass

