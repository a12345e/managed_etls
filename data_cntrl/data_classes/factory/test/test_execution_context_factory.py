import unittest
from datetime import datetime, timedelta
import pytest

from data_cntrl.data_classes.factory.execution_context_factory import create_execution_context
from data_cntrl.data_classes.factory.component_id_factory import create_component_id_number_description

start = datetime.now()


class ExecutionContextCreateTest(unittest.TestCase):

    @staticmethod
    def test_execution_context_factory_positive():
        e = create_execution_context(principal='alon', shift_start=start,
                                     shift_end=start+timedelta(days=1),
                                     infrastructure_task='action=1000',
                                     mission=create_component_id_number_description("production_zorem",1.1,
                                                                                    "the zorem stuff"),
                                     application=create_component_id_number_description("default",1.1,
                                                                                        "the default application"))
        assert e.principal == 'alon'
        assert e.shift_start == start
        assert e.shift_end == start + timedelta(days=1)
        assert e.infrastructure_task == 'action=1000'
        assert e.mission.name == "production_zorem"
        assert e.mission.version == 1.1
        assert e.mission.description == "the zorem stuff"
        assert e.application.name == 'default'
        assert e.application.version == 1.1
        assert e.application.description == "the default application"

    @staticmethod
    def test_short_string():
        with pytest.raises(ValueError):
            create_execution_context(principal='n', shift_start=start,
                                     shift_end=start + timedelta(days=1),
                                     infrastructure_task='action=1000',
                                     mission=create_component_id_number_description("production_zorem", 1.1,
                                                                                    "the zorem stuff"),
                                     application=create_component_id_number_description("default", 1.1,
                                                                                        "the default application"))


def test_missing_shift_end():
    with pytest.raises(ValueError):
        create_execution_context(principal='hey', shift_start=start,
                                 shift_end=None,
                                 infrastructure_task='action=1000',
                                 mission=create_component_id_number_description("production_zorem", 1.1,
                                                                                "the zorem stuff"),
                                 application=create_component_id_number_description("default", 1.1,
                                                                                    "the default application"))


if __name__ == '__main__':
    unittest.main()
