from typing import Sequence
from infra.abstracts.operator.etl import ETL
from infra.abstracts.operator.sensor import Sensor
from infra.abstracts.mng.principal import Principal
from datetime import datetime


class ShiftPolicy:
    def __init__(self,
                 realm: Principal,
                 shift_start: datetime,
                 shift_end: datetime,
                 operators: Sequence[ETL],
                 sensors: Sequence[Sensor]):
        """
        It is the shift of the principal to take place implementing the above policy, and the principal must never
        start any new operator outside the shift time by means of the real time clock. So if the shift does not
        coincide with the current clock time the principal will do nothing and backoff.
        The principal should complete all the operations it had
        started with in the shift and there is no limit to finish them.

        The principal entering at valid shift must take the following measures,
        1) Check that there is no other same principal on shift duty, otherwise
        it must log and error that return immediately with failure.
        2) Check for zombie operator, namely operations that show death signs and had started at previous shift.
           It is closing them as used operations ending with failure
        3) Check for product names that have more than one instance in ready state.
            If not than try to keep the one that currently being created or used, and remove the rest, with error report
            If none is currently used or on creation than keep the oldest and report error
        4) Run in a loop:
            Iff we are within our shift:
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
