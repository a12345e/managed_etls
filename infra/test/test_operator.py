import unittest
from infra.operator import Operator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        operator = Operator("myoperator","1.1","initial")
        self.assertEqual(operator.name,"myoperator")  # add assertion here
        self.assertEqual(operator.version_number,"1.1")  # add assertion here
        self.assertEqual(operator.version_description,"initial")  # add assertion here

if __name__ == '__main__':
    unittest.main()
