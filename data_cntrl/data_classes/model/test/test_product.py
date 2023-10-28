import unittest
from data_cntrl.data_classes.model.product import Product


class ProductTest(unittest.TestCase):
    @staticmethod
    def test_positive():
        p = Product(name='name1', store='store1', operator='operator1', batch='batch1')
        assert p.name == 'name1'
        assert p.store == 'store1'
        assert p.operator == 'operator1'
        assert p.batch == 'batch1'


if __name__ == '__main__':
    unittest.main()
