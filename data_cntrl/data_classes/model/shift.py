import datetime
import pydantic
from typing_extensions import Annotated


class Shift(pydantic.BaseModel):
    start: datetime.datetime
    end: datetime.datetime
