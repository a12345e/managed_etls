from datetime import datetime
import unittest
from data_cntrl.data_classes.model.operation import Operation
from operators.test.my_sensor import MySensor
from data_cntrl.data_classes.model.product import Product
from application.abstract.application import Context


class MyTestCase(unittest.TestCase):
    def test_something(self):
        operator = MySensor("my_test_sensor", '1.1', "hey")
        mission = Product("realm1", 'alon', 'my_batch')
        now = datetime.now()
        op = Operation('principal', mission, now)
        self.assertEqual(op.principal, )  # add assertion here
        self.assertEqual(op.principal, Context.TEST)  # add assertion here
        self.assertEqual(op.mission.name, "my_test_sensor")  # add assertion here
        self.assertEqual(op.mission.batch, "my_batch")  # add assertion here


if __name__ == '__main__':
    unittest.main()
