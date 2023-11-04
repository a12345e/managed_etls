import unittest
import pytest
from data_cntrl.data_classes.factory.component_id_factory import create_component_id, create_component_id_number, \
                                                                  create_component_id_number_description


class ComponentIDCreateTest(unittest.TestCase):
    @staticmethod
    def test_positive_all_parameters():
        c = create_component_id_number_description('name1', '1.1', 'some')
        assert c.name == 'name1'
        assert c.version == '1.1'
        assert c.description == 'some'

    @staticmethod
    def test_positive_just_id():
        c = create_component_id('name1')
        assert c.name == 'name1'

    @staticmethod
    def test_positive_just_id_number():
        c = create_component_id_number('name1', 1.1)
        assert c.name == 'name1'
        assert c.version == 1.1

    @staticmethod
    def test_positive_just_id_number_string():
        c = create_component_id_number('name1', '1.1')
        assert c.name == 'name1'
        assert c.version == '1.1'

    @staticmethod
    def test_short_name():
        with pytest.raises(ValueError):
            create_component_id_number('na', 1.1)

    @staticmethod
    def test_NULL_name():
        with pytest.raises(ValueError):
            create_component_id_number(None, 1.1)

    @staticmethod
    def test_boolean_number():
        with pytest.raises(ValueError):
            create_component_id_number('aaaa', False)

    @staticmethod
    def test_none_number():
        with pytest.raises(ValueError):
            create_component_id_number('dddd', None)

    @staticmethod
    def test_none_description():
        with pytest.raises(ValueError):
            create_component_id_number('xxx', None)


if __name__ == '__main__':
    unittest.main()
