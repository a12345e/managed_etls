from abc import ABC, abstractmethod
from typing import Sequence
import string
from datetime import datetime
from infra.operation import Operation, Product


class OperationsStore(ABC):

    @abstractmethod
    def get_operations(self, after: datetime) -> Sequence[Operation]:
        pass
    @abstractmethod
    def get_operations(self, phase: Operation.PHASE) -> Sequence[Operation]:
        pass
    @abstractmethod
    def get_operations(self, ids: Sequence[string]) -> Sequence[Operation]:
        pass
    @abstractmethod
    def create_operations(self, operations: Sequence[Operation]):
        pass

    @abstractmethod
    def update_operations(self, operations: Sequence[Operation]):
        pass

