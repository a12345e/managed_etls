from typing import Sequence
from etl.etl_operator import  ETLOperator
from etl.sensor_operator import  SensorOperator
from manager.realm import  Realm
class ShiftPolicy:
    def __init__(self,
                 realm: Realm,
                 operators: Sequence[ETLOperator],
                 sensors: Sequence[SensorOperator]):
        pass