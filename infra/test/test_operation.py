from datetime import datetime
import unittest
from infra.operation import Operation
from infra.abstracts.operator.sensor import Sensor
from infra.product import Product
from infra.principal import Principal


class MyTestCase(unittest.TestCase):
    def test_something(self):
        principal = Principal.TEST
        operator = Sensor(name="my_test_sensor", version_number='1.1', version_description="hey")
        mission = Product(operator, 'alon', 'my_batch')
        now = datetime.now()
        op = Operation(principal, mission, now)
        self.assertEqual(op.principal, Principal.TEST)  # add assertion here
        self.assertEqual(op.principal, Principal.TEST)  # add assertion here
        self.assertEqual(op.mission.name, "my_test_sensor")  # add assertion here
        self.assertEqual(op.mission.batch, "my_batch")  # add assertion here


if __name__ == '__main__':
    unittest.main()
