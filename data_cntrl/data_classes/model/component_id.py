import pydantic
from typing_extensions import Annotated
from typing import Optional


class ComponentId(pydantic.BaseModel):
    name: Annotated[str, pydantic.StringConstraints(min_length=3)]
    version: Annotated[str, pydantic.StringConstraints(min_length=3)] | pydantic.PositiveFloat = None
    description: Annotated[str, pydantic.StringConstraints(min_length=3)] = None
