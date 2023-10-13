from typing import Sequence
from etl_operator import ETLOperator
from sensor_operator import SensorOperator
from manager.principal import Principal
from datetime import datetime


class ShiftPolicy:
    def __init__(self,
                 realm: Principal,
                 shift_start: datetime,
                 shift_end: datetime,
                 operators: Sequence[ETLOperator],
                 sensors: Sequence[SensorOperator]):
        """
        It is the shift of the principal to take place implementing the above policy, and the principal must never
        start any new operation outside the shift time by means of the real time clock. So if the shift does not
        coincide with the current clock time the principal will do nothing and backoff.
        The principal should complete all the operations it had
        started with in the shift.

        The principal entering at valid shift must take the following measures,
        1) Check that there is no other concurrent principal at the same principal with an incumbent shift, otherwise
        it Must log and error that return immediately with failure.
        2) Check for zombie operation, namely operations that show death signs and had started at previous shift.
           It is closing them as used operations ending with failure
        3) Check for product names that have more than one instance that is not used already. If not keep the oldest.
        Run in a loop:
            If we are withing our shift:
                Learn what are the new missions available.
                Run new missions with multithreading
                learn what operations are already fully used and mark them as used


        :param realm:
        :param shift_start:
        :param shift_end:
        :param operators:
        :param sensors:
        """
        pass
