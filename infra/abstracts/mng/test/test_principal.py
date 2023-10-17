import unittest
from infra.abstracts.mng.principal import Principal

class MyTestCase(unittest.TestCase):
    def test_principal_test(self):
        p = Principal.TEST
        self.assertEqual(p, Principal.TEST)  # add assertion here

    def test_principal_production(self):
        p = Principal.PRODUCTION
        self.assertEqual(p, Principal.PRODUCTION)  # add assertion here


if __name__ == '__main__':
    unittest.main()
