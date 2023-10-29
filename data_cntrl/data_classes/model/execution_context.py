import pydantic
from data_cntrl.data_classes.model.principal import Principal
from data_cntrl.data_classes.model.shift import Shift
from data_cntrl.data_classes.model.application import Application


class ExecutionContext(pydantic.BaseModel):
    principal: Principal
    application: Application
    shift: Shift

