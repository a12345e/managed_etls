import pydantic
from datetime import datetime
from typing_extensions import Annotated
from data_cntrl.data_classes.model.component_id import ComponentId


class ExecutionContext(pydantic.BaseModel):
    principal:  Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]
    shift_start: datetime
    shift_end: datetime
    infrastructure_task: Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]
    mission: ComponentId
    application: ComponentId

