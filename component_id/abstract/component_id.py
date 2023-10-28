import pydantic
from typing_extensions import Annotated

class ComponentId(pydantic.BaseModel):
    name: Annotated[str, pydantic.StringConstraints(min_length=3)]
    number: Annotated[str, pydantic.StringConstraints(min_length=3)] | pydantic.PositiveFloat | None
    description: pydantic.StrictStr | None
