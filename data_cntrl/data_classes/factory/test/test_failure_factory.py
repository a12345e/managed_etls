import unittest
import pytest

from data_cntrl.data_classes.factory.failure_factory import create_failure


class FailureCreateTest(unittest.TestCase):
    @staticmethod
    def test_failure_factory_positive():
        f = create_failure(category='circuit_breaker', details=['timeout=5', 'reason= not enough resources'])
        assert f.category == 'circuit_breaker'
        assert f.details == ['timeout=5', 'reason= not enough resources']

    @staticmethod
    def test_short_string():
        with pytest.raises(ValueError):
            create_failure(category='cddd', details=['ti', 'reason= not enough resources'])


if __name__ == '__main__':
    unittest.main()
