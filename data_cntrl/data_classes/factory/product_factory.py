from data_cntrl.data_classes.model.product import Product


def create_product(name: str, store: str, function: str, batch: str):
    return Product(name=name, store=store, function=function, batch=batch)