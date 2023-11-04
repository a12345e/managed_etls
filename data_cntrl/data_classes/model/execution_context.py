import pydantic
from datetime import datetime
from data_cntrl.data_classes.model.component_id import ComponentId


class ExecutionContext(pydantic.BaseModel):
    principal:  pydantic.Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]
    shift_start: datetime
    shift_end: datetime
    infrastructure_task: pydantic.Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]
    mission: ComponentId
    application: ComponentId

