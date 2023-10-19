from abc import ABC
from typing import final
import string
from infra.operator import Operator
from infra.realm import Realm


@final
class Product(ABC):
    """
       The product is a tuple (realm, operator, name, and batch).
       Unlike the operation the product stands for the very object materialized by the operation.
       The product is part of the data plane not the control data plane of the operations
       - realm is the data level realm, like where is the data stored, e.g. test/production
       - the operator who is doing the operation and this is part of the product definition
       - the name of the concrete specific product, as there is no limit to the number products for each operator
       - the specific batch of the product
    """
    def __init__(self, realm: Realm,
                 operator: Operator,
                 name: string,
                 batch: string):
        self._realm = realm
        self._operator = operator
        self._name = name
        self._batch = batch

    @property
    def realm(self):
        return self._realm

    @property
    def operator(self):
        return self._operator

    @property
    def name(self):
        return self._name

    @property
    def batch(self):
        return self._batch
