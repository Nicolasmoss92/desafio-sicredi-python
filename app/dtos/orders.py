from typing import Annotated

from pydantic import BaseModel, Field

PositiveInt = Annotated[int, Field(gt=0)]


class CombineOrdersRequestDTO(BaseModel):
    requests: list[PositiveInt] = Field(
        ..., description="Lista de valores monetários requisitados pelas agências"
    )
    n_max: int = Field(..., gt=0, description="Valor máximo permitido por viagem")


class CombineOrdersResponseDTO(BaseModel):
    total_trips: int = Field(..., description="Número mínimo de viagens necessárias")
