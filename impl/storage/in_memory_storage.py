import string
from datetime import datetime
from typing import Sequence, Callable

from infra.operation import Operation
from infra.abstracts.storage.operations_store import OperationsStore


class InMemoryOperationsStorage(OperationsStore):

    def __init__(self):
        self._operations_map = {}

    def get_operations(self, filter: Callable) -> Sequence[Operation]:
        return filter(lambda operation: filter, self._operations_map.values())

    def create_operations(self, operations: Sequence[Operation]) -> Sequence[Operation]:
        for operation in operations:
            if operation.id in self._operations_map.keys():
                raise Exception("Operation id " + operation.id + " already exists")
            self._operations_map[operation.id] = operation

    def update_operations(self, operations: Sequence[Operation]):
        for operation in operations:
            if operation.id not in self._operations_map.keys():
                raise Exception("Operation id " + operation.id + " does not exist")
            self._operations_map[operation.id] = operation
        pass
