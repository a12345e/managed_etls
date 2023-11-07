from data_cntrl.data_classes.model.realm import Realm
from data_cntrl.data_classes.model.product import Product
from data_cntrl.data_classes.model.execution_context import ExecutionContext
from data_cntrl.data_classes.model.operation import Operation


def create_operation(
        realm: Realm,
        product: Product,
        execution_context: ExecutionContext):
    return Operation(realm=realm, product=product, execution_context=execution_context)
