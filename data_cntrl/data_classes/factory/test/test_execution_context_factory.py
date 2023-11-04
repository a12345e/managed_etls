import unittest

import pytest

from data_cntrl.data_classes.factory.execution_context_factory import create_execution_context


class ExecutionContextCreateTest(unittest.TestCase):
    @staticmethod
    def test_execution_context_factory_positive():
        f = create_execution_context(principal='alon',category='circuit_breaker', details=['timeout=5', 'reason= not enough resources'])
        assert f.category == 'circuit_breaker'
        assert f.details == ['timeout=5', 'reason= not enough resources']

    @staticmethod
    def test_short_string():
        with pytest.raises(ValueError):
            create_execution_context(category='cddd', details=['ti', 'reason= not enough resources'])


if __name__ == '__main__':
    unittest.main()
