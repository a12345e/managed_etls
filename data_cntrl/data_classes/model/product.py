import pydantic
from typing_extensions import Annotated


class Product(pydantic.BaseModel):
    name: Annotated[str, pydantic.StringConstraints(min_length=3)]
    store: Annotated[str, pydantic.StringConstraints(min_length=3)]
    operator: Annotated[str, pydantic.StringConstraints(min_length=3)]
    batch: Annotated[str, pydantic.StringConstraints(min_length=3)]



