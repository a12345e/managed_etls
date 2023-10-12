from datetime import datetime
from typing import final
from manager.realm import Realm
from common.product import Product
from typing import Final


@final
class ETLOperation:
    def __init__(self,
                 realm: Realm,
                 mission: Product,
                 create_time: datetime):
        self._realm: Final[Realm] = realm
        self.mission: Final[Product] = mission
        self._create_time: Final[datetime] = create_time

    @property
    def realm(self):
        return self._realm

    @property
    def mission(self):
        return self._mission

    @property
    def create_time(self):
        return self._create_time
