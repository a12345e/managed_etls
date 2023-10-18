from datetime import datetime


class Shift:
    def __init__(self, start: datetime, end: datetime):
        self._start = start
        self._end = end
