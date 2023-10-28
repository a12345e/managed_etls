from abc import ABC


class OperationsManager(ABC):
    """
    Initialize:
        create all operators objects, etl ones and sensors
            It is the shift of the principal to take place implementing the principal policy,
            and the principal must never
            start any new operators outside the shift time by means of the real time clock. So if the shift does not
            coincide with the current clock time the principal will do nothing and backoff.
            The principal should complete all the operations it had
            started with in the shift and there is no limit to finish them.

            The principal entering at valid shift must take the following measures,
            1) Check that there is no other same principal on shift duty, otherwise
            it must log and error that return immediately with failure.
            2) Check for zombie operators, namely operations that show death signs and had started at previous shift.
               It is closing them as used operations ending with failure
            3) Check for product names that have more than one instance in ready state.
                If not than try to keep the one that currently being created or used, and remove the rest, with error report
                If none is currently used or on creation than keep the oldest and report error
            4) Run in a loop:
                Iff we are within our shift:
                    Learn what are the new missions available.
                    Run new missions with multithreading
                    learn what operations are already fully used and mark them as used


    :param es:
    :return:
    """

    pass
