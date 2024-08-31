from pydantic import BaseModel


class Model(BaseModel):
    field: str


def func(value: str) -> Model:
    return Model(field=value)
