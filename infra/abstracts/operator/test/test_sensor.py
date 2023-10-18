import unittest
from infra.abstracts.operator.test.my_sensor import MySensor
from infra.abstracts.mng.principal import Principal


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sensor = MySensor("my_sensor","1.1","aaaa")
        self.assertEqual(sensor.name, "my_sensor")  # add assertion here
        p = Principal.TEST
        products = sensor.discover(p)
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].name, "product1")
        self.assertEqual(products[1].name, "product2")


if __name__ == '__main__':
    unittest.main()
