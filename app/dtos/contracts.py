from pydantic import BaseModel, Field


class ContractDTO(BaseModel):
    id: int = Field(..., gt=0, description="Identificador do correntista")
    debt: float = Field(..., ge=0, description="Saldo devedor total do correntista")


class TopContractsRequestDTO(BaseModel):
    open_contracts: list[ContractDTO] = Field(
        ..., description="Lista de contratos em aberto"
    )
    renegotiated_contracts: list[int] = Field(
        ..., description="IDs dos contratos já renegociados"
    )
    top_n: int = Field(..., gt=0, description="Quantidade de devedores a retornar")


class TopContractsResponseDTO(BaseModel):
    top_debtors: list[int] = Field(
        ..., description="IDs dos maiores devedores ordenados do maior para o menor"
    )
