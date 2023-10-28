import unittest
from application.abstract.application import Context
from typing import List


class Production(Context):
    def __init__(self, name: str, realm: str, etls: List[str], sensors: List[str]):
        super().__init__(name,realm, etls, sensors)
        pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = Production('x','y', [], [])
        self.assertEqual(p.name, 'x', [])  # add assertion here
        self.assertEqual(p.realm, 'y', [])  # add assertion here



if __name__ == '__main__':
    unittest.main()
