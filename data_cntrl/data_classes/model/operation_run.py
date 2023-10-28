import datetime
import pydantic
from typing import List, TypedDict

class OperationRun(pydantic.BaseModel):
    start: pydantic.PastDatetime | None
    end: pydantic.PastDatetime | None
    trace: List[str] = []
    metrics: pydantic.Dic