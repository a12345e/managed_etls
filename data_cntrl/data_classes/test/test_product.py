import unittest
from data_cntrl.data_classes.model.product import Product


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = Product("realm1","operator1", "product1", "20230101")
        self.assertEqual(p.realm,"realm1")  # add assertion hereself.assertEqual(p.name,"myoperator")  # add assertion here
        self.assertEqual(p.name, "product1")  # add assertion here
        self.assertEqual(p.name, "product1")  # add assertion here
        self.assertEqual(p.batch, "20230101")  # add assertion here


if __name__ == '__main__':
    unittest.main()
