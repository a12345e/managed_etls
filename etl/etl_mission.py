from common.product import Product
from typing import Final

class ETLMission:
    """
    A mission is what we are about to do. Other than that it is just a product.
    """
    def __init__(self,
                 product: Product):
        """
        :param product:
        """
        self._product : Final[Product] = product

    @property
    def product(self):
        return self._product


