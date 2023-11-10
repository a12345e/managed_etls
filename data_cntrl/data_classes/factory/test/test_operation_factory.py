import unittest
import pytest
from datetime import datetime, timedelta
from data_cntrl.data_classes.model.realm import Realm
from data_cntrl.data_classes.factory.operation_factory import create_operation
from data_cntrl.data_classes.factory.product_factory import create_product
from data_cntrl.data_classes.factory.execution_context_factory import create_execution_context
from data_cntrl.data_classes.factory.component_id_factory import create_component_id_number_description

start = datetime.now()


class OperationCreateTest(unittest.TestCase):
    @staticmethod
    def test_positive():
        product = create_product(realm=Realm.TEST, name='name1', store='store1', function='func1', batch='batch1')
        execution_context = create_execution_context(principal='alon', shift_start=start,
                                                     shift_end=start + timedelta(days=1),
                                                     infrastructure_task='action=1000',
                                                     mission=create_component_id_number_description("production_zorem",
                                                                                                    1.1,
                                                                                                    "the zorem stuff"),
                                                     application=create_component_id_number_description("default", 1.1,
                                                                                                       "the default application"))
        operation = create_operation(Realm.TEST, product, execution_context)
        assert operation.realm == Realm.TEST
        assert operation.product.store == 'store1'
        assert operation.execution_context.shift_end == start + timedelta(days=1)

    @staticmethod
    def test_short_name():
        with pytest.raises(ValueError):
            product = create_product(name='name1', store='store1', function='func1', batch='batch1')
            execution_context = create_execution_context(principal='alon', shift_start=start,
                                                         shift_end=start + timedelta(days=1),
                                                         infrastructure_task='action=1000',
                                                         mission=create_component_id_number_description(
                                                             "production_zorem", 1.1,
                                                             "the zorem stuff"),
                                                         application=create_component_id_number_description("default",
                                                                                                            1.1,
                                                                                                            "the default application"))

            operation = create_operation(Realm.TEST, product)


if __name__ == '__main__':
    unittest.main()
