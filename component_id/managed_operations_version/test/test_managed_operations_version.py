import unittest
from component_id.managed_operations_version.managed_operations_version import managed_operations_version


class MyTestCase(unittest.TestCase):
    def test_version(self):
        assert managed_operations_version.name == 'ManagedOperations'


if __name__ == '__main__':
    unittest.main()
