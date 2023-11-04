from data_cntrl.data_classes.model.execution_context import ExecutionContext
from data_cntrl.data_classes.model.component_id import ComponentId
from datetime import datetime


def create_execution_context(principal: str, shift_start: datetime, shift_end: datetime, infrastructure_task: str,
                             mission: ComponentId, application: ComponentId):
    return ExecutionContext(principal=principal, shift_start=shift_start, shift_end=shift_end,
                            infrastructure_task=infrastructure_task, mission=mission, application=application)
