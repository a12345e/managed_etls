import datetime
import pydantic
from typing_extensions import Annotated


class Shift(pydantic.BaseModel):
    start: Annotated[datetime.datetime, pydantic.PastDatetime]
    end: Annotated[datetime.datetime, pydantic.FutureDatetime]
