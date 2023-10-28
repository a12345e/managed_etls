import pydantic
from typing_extensions import  Annotated


class Principal(pydantic.BaseModel):
    person: Annotated[str, pydantic.StringConstraints(min_length=3)]
    task: Annotated[str, pydantic.StringConstraints(min_length=3)]
    detailed: Annotated[str, pydantic.StringConstraints(min_length=3)] | None

