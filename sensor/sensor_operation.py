from datetime import datetime
from typing import final
from etl.realm import Realm
from etl.etl_mission import ETLMission
from sensor.sensor_mission import SensorMission
from typing import Final

@final
class SensorOperation:
    def __init__(self,realm: Realm, mission: SensorMission, create_time: datetime):
        self._realm: Final[Realm] = realm
        self.mission: Final[ETLMission] = mission
        if self.mission.product.source_operations:
            raise Exception("there are no source raw materials for products create by a sensor")
        self._create_time:  Final[datetime] = create_time
    @property
    def realm(self):
        return self._realm
    @property
    def mission(self):
        return self._mission
    @property
    def create_time(self):
        return self._create_time

