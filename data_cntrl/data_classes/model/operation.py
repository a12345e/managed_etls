from datetime import datetime
import pydantic
from typing import List, Dict
from enum import Enum
from data_cntrl.data_classes.model.product import Product
from data_cntrl.data_classes.model.execution_context import ExecutionContext
from data_cntrl.data_classes.model.failure import Failure


class OPERATION_PHASE(Enum):
    CREATING = 1
    READY = 2
    FAILED = 3
    IGNORED = 4
    POTENTIAL_USING_PRODUCTS_ARE_CREATED = 5
    ALL_RESOURCE_PRODUCTS_ARE_FULLY_USED = 6


class Operation(pydantic.BaseModel):
    product: Product
    execution_context: ExecutionContext
    phases: Dict[OPERATION_PHASE, datetime]
    using_operations: List[str]
    used_by_operations: List[str] = []
    execution_context: ExecutionContext
    trace: List[Dict[datetime.datetime, str]] = []
    product_metrics: Dict[str, pydantic.StrictFloat]
    success: pydantic.StrictBool | None
    failure: Failure | None

