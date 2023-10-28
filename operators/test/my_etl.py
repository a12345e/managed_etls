import typing

from application.abstract.application import Context
from operators.etl.abstract.etl import Etl
from data_cntrl.data_classes.model import Product
from data_cntrl.data_classes.model import Operation


class MyEtl(Etl):

    def usable_products(self, ready_raw_materials: typing.Sequence[Product]) -> (
            typing.Sequence)[Product]:
        return [x for x in ready_raw_materials if x.name == 'product1' and x.operator.name == 'myoperator1'] + \
        [x for x in ready_raw_materials if x.name == 'product2' and x.operator.name == 'myoperator2']

    def ready_missions(self, ready_raw_materials: typing.Sequence[Product]) -> typing.Sequence[Product]:
        return [x for x in ready_raw_materials if x.name == 'product1' and x.operator.name == 'myoperator1']
        pass

    def execute(self, principal: Context, mission: Product) -> Operation:
        pass


