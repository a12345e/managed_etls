from abc import ABC, abstractmethod
from typing import Sequence, Callable
from data_cntrl.data_classes.model import Operation


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

