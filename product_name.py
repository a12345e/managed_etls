from typing import final, Final, Sequence
import string


@final
class ProductName:
    """
       The product name is the essence of the product namely the 'name' and batch of the products, namely partition
       as in our case it will be the specific batch
    """
    def __init__(self, name: string,
                 partition: string):
        self._name: Final[string] = name
        self._partition: Final[string] = partition

    @property
    def name(self):
        return self._name

    @property
    def partition(self):
        return self._partition
