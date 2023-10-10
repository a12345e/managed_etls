from typing import Final, Sequence
import string
from etls.product import Product
from etls.etl_operator import ETLOperator
from etls.etl_operation import ETLOperation
from etls.realm import Realm


class ETLMission:
    """
    A mission is what we are about to do.
    We are about to use a tool namely the etl_operator to create a product namely the product.
    Yet our subject is the operation not the result of the operation (namely the product)
    as all we do is 'do and remember what we do'. So we also, keep track not of the raw materials of our operation
    but of the operations that took place to create our raw materials.
    """
    def __init__(self,
                 realm: Final[Realm],
                 etl_operator: Final[ETLOperator],
                 product: Product,
                 source_operations: Sequence[ETLOperation]):
        """

        :param realm:
        :param etl_operator:
        :param product:
        :param source_operations:
        """
        pass
