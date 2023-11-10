from data_cntrl.data_classes.model.product import Product
from data_cntrl.data_classes.model.realm import Realm


def create_product(realm: Realm, name: str, store: str, function: str, batch: str):
    return Product(name=name, store=store, function=function, batch=batch)