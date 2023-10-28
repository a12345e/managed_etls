from data_cntrl.data_classes.model.product import Product


def create_product( name: str, store: str,operator: str, batch: str):
    return Product(name=name, store=store, operator=operator, batch=batch)