import datetime
from typing import Sequence

from application.abstract.application import Context
from functions.etl.abstract.sensor import Sensor
from data_cntrl.data_classes.model import Product
from data_cntrl.data_classes.model import Operation


class MySensor(Sensor):

    def discover(self, principal: Context, start_time: datetime = None, end_time: datetime.datetime = None) -> \
            Sequence[Operation]:
        p1 = Product("production","myoperator1", "product1", "20230101")
        p2 = Product("production", "myoperator1","product2", "20230101")
        return [p1,p2]
