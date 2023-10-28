from datetime import datetime, timedelta
import unittest
from operators.test.my_sensor import MySensor
from application.abstract.application import Context


class Plala(Context):
    def __init__(self, name: str, realm: str, etls: [str], sensors: [str]):
        super().__init__('')
    pass


class MyTestCase(unittest.TestCase):

    def test_something(self):
        sensor = MySensor("my_sensor","1.1","aaaa")
        self.assertEqual(sensor.name, "my_sensor")  # add assertion here
        principal = Plala('production','test',[],[])
        now = datetime.now()
        products = sensor.discover(principal, now, now + timedelta(hours=1))
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].name, "product1")
        self.assertEqual(products[1].name, "product2")


if __name__ == '__main__':
    unittest.main()
