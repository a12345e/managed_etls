import unittest
import pytest
from data_cntrl.data_classes.factory.product_factory import create_product


class ProductCreateTest(unittest.TestCase):
    @staticmethod
    def test_positive():
        p = create_product(name='name1', store='store1', function='func1', batch='batch1')
        assert p.name == 'name1'
        assert p.store == 'store1'
        assert p.function == 'func1'
        assert p.batch == 'batch1'

    @staticmethod
    def test_short_name():
        with pytest.raises(ValueError):
            create_product(name='na', store='store1', function='func1', batch='batch1')


if __name__ == '__main__':
    unittest.main()
