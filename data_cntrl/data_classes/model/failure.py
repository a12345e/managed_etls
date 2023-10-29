import pydantic
from typing import Dict
from typing import List, Annotated


class Failure(pydantic.BaseModel):
    category: Annotated[str, pydantic.StringConstraints(min_length=3)]
    details: Annotated[str, pydantic.StringConstraints(min_length=3)] | None
