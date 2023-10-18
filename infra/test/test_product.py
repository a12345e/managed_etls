import unittest
from infra.operator import Operator
from infra.product import Product


class MyTestCase(unittest.TestCase):
    def test_something(self):
        operator = Operator("myoperator", "1.1", "initial")
        p = Product(operator, "product1", "20230101")
        self.assertEqual(p.operator.name,"myoperator")  # add assertion here
        self.assertEqual(p.name, "product1")  # add assertion here
        self.assertEqual(p.batch, "20230101")  # add assertion here


if __name__ == '__main__':
    unittest.main()
