import datetime
from abc import ABC, abstractmethod
from typing import final, Final
from etls.product import Product
from etls.etl_operator import ETLOperator
import string


@final
class ETLOperation:
    def __init__(self,
                 realm: Final[string],
                 etl_operator: Final[ETLOperator],
                 product: Product):
        self._realm: Final[string] = realm
        self._product: Final[Product] = product
        self.etl_operator: Final[ETLOperator] = etl_operator
        self._create_time = None

    @property
    def realm(self):
        return self._realm

    @property
    def etl_operator(self):
        return self._etl_operator

    @property
    def product(self):
        return self._product

