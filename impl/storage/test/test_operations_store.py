import unittest
from infra.operation import Operation
from infra.abstracts.operator.sensor import Sensor
from impl.storage.in_memory_storage import InMemoryOperationsStorage
from infra.product import Product
from infra.abstracts.storage.operations_store import OperationsStore
from infra.principal import Principal


def filter(x : Operation):
    x.principal == Principal.TEST
class MyTestCase(unittest.TestCase):
    def test_something(self):
        op = Operation(principal=Principal.TEST,
                       mission=Product(
                           operator=Sensor(name="my_test_sensor", version_number='1.1', version_description="hey"),
                           name='alon',
                           batch='my_batch')
                       )
        store: OperationsStore = InMemoryOperationsStorage()
        store.create_operations([op])
        result = store.get_operations(filter)
        self.assertEqual(1, len(result))  # add assertion here

if __name__ == '__main__':
    unittest.main()
