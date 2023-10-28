import unittest
from infra.realm import Realm


class Prod(Realm):
    def __init__(self, name: str):
        super().__init__(name)
        pass


class MyTestCase(unittest.TestCase):
    def test_something(self):

        realm = Prod('x')
        self.assertEqual(realm.name, 'x')  # add assertion here


if __name__ == '__main__':
    unittest.main()
