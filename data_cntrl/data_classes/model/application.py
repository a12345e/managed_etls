import pydantic
from typing_extensions import  Annotated


class Application(pydantic.BaseModel):
    name: Annotated[str, pydantic.StringConstraints(min_length=3)]
    purpose: Annotated[str, pydantic.StringConstraints(min_length=3)]
