import pydantic
from typing import Sequence
from typing_extensions import  Annotated


class Failure(pydantic.BaseModel):
    category: Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]
    details:  Sequence[Annotated[pydantic.StrictStr, pydantic.StringConstraints(min_length=3)]]
