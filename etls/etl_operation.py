from datetime import datetime
from abc import ABC, abstractmethod
from typing import final, Final
from etls.product import Product
from etls.realm import Realm
from etls.etl_mission import ETLMission
from etls.etl_operator import ETLOperator
import string


@final
class ETLOperation:
    def __init__(self, mission: ETLMission, create_time: datetime):
        self.mission: ETLMission = mission
        self._create_time:  datetime = create_time
    @property
    def mission(self):
        return self._mission
    @property
    def create_time(self):
        return self._create_time

