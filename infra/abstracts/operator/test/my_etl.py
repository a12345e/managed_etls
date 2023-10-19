import datetime
import typing
from typing import Sequence

from infra.principal import Principal
from infra.abstracts.operator.etl import Etl
from infra.operator import Operator
from infra.product import Product
from infra.operation import Operation


class MyEtl(Etl):

    def usable_products(self, ready_raw_materials: typing.Sequence[Product]) -> (
            typing.Sequence)[Product]:
        return [x for x in ready_raw_materials if x.name == 'product1' and x.operator.name == 'myoperator1'] + \
        [x for x in ready_raw_materials if x.name == 'product2' and x.operator.name == 'myoperator2']

    def ready_missions(self, ready_raw_materials: typing.Sequence[Product]) -> typing.Sequence[Product]:
        return [x for x in ready_raw_materials if x.name == 'product1' and x.operator.name == 'myoperator1']
        pass

    def execute(self, principal: Principal, mission: Product) -> Operation:
        pass


