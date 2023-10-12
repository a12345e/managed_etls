from typing import Sequence
from etl.etl_operator import ETLOperator
from etl.sensor_operator import SensorOperator
from manager.realm import Realm
from datetime import datetime


class ShiftPolicy:
    def __init__(self,
                 realm: Realm,
                 shift_start: datetime,
                 shift_end: datetime,
                 operators: Sequence[ETLOperator],
                 sensors: Sequence[SensorOperator]):
        pass
