import unittest
import pytest
from component_id.abstract.component_id import ComponentId


class MyTestCase(unittest.TestCase):
    def test_positive(self):
        c = ComponentId(name='name1', number=1.1, description='aaa')
        assert c.name == 'name1'
        assert isinstance(c.name, str)
        assert c.number == 1.1
        assert isinstance(c.number, float)
        assert c.description == 'aaa'
        assert isinstance(c.name, str)

    @staticmethod
    def test_invalid_number():
        with pytest.raises(ValueError):
            p = ComponentId(name='xxx', number=-1.1, description='aaa')

    @staticmethod
    def test_short_name():
        with pytest.raises(ValueError):
            p = ComponentId(name='xx', number=-1.1, description='aaa')

    @staticmethod
    def test_short_description():
        with pytest.raises(ValueError):
            p = ComponentId(name='xx', number=-1.1, description='sd')

if __name__ == '__main__':
    unittest.main()
