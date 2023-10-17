import datetime
from typing import Sequence

from infra.abstracts.mng.principal import Principal
from infra.abstracts.operator.sensor import Sensor
from infra.operator import Operator
from infra.product import Product
from infra.operation import Operation


class MySensor(Sensor):

    def discover(self, principal: Principal, start_time: datetime = None, end_time: datetime.datetime = None) -> \
            Sequence[Operation]:
        operator = Operator("myoperato1", "1.1", "initial1")
        p1 = Product(operator, "product1", "20230101")
        operator = Operator("myoperator2", "2.2", "initial2")
        p2 = Product(operator, "product2", "20230101")
        return [p1,p2]
