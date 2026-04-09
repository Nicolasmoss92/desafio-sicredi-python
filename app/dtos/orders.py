from pydantic import BaseModel, Field


class CombineOrdersRequestDTO(BaseModel):
    requests: list[int] = Field(
        ..., description="Lista de valores monetários requisitados pelas agências")
    n_max: int = Field(..., gt=0, description="Valor máximo permitido por viagem")


class CombineOrdersResponseDTO(BaseModel):
    total_trips: int = Field(..., description="Número mínimo de viagens necessárias")
