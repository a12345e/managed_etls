from datetime import datetime
import pydantic
from typing import List, Dict, Tuple
from enum import Enum
from data_cntrl.data_classes.model.product import Product
from data_cntrl.data_classes.model.execution_context import ExecutionContext
from data_cntrl.data_classes.model.failure import Failure
from data_cntrl.data_classes.model.realm import Realm


class OPERATION_PHASE(Enum):
    CREATING = 1
    READY = 2
    COMPLETE_SUCCESS = 5
    COMPLETE_FAIL = 6
    COMPLETE_IGNORE = 7


class Operation(pydantic.BaseModel):
    realm: Realm
    product: Product
    execution_context: ExecutionContext
    current_phase_value: OPERATION_PHASE
    current_phase_start_time: datetime
    phases_history: Dict[OPERATION_PHASE, datetime] = []
    depending_on_operation_ids: List[pydantic.Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]] \
        = []
    used_by_operation_ids: List[str] = []
    trace: List[Tuple[datetime.datetime, str]] = []
    product_metrics: Dict[pydantic.Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)], \
        pydantic.StrictFloat] = []
    failure: Failure | None
