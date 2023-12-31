import unittest
import pytest
from data_cntrl.data_classes.model.product import Product


class ProductTest(unittest.TestCase):
    @staticmethod
    def test_positive():
        p = Product(name='name1', store='store1', function='func1', batch='batch1')
        assert p.name == 'name1'
        assert p.store == 'store1'
        assert p.function == 'func1'
        assert p.batch == 'batch1'

    @staticmethod
    def test_short_name():
        with pytest.raises(ValueError):
            Product(name='na', store='store1', funcion='func2', batch='batch1')


if __name__ == '__main__':
    unittest.main()
