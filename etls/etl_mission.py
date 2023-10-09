from typing import Final, Sequence
import string
from etls.product import Product
from etls.etl_operator import ETLOperator
from etls.etl_operation import ETLOperation


class ETLMission:
    def __init__(self,
                 etl_operator: Final[ETLOperator],
                 product: Product,
                 depending_etl_operations: Sequence[ETLOperation]):
        pass
