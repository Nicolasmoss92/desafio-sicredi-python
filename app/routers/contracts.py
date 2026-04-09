from fastapi import APIRouter

from app.dtos.contracts import TopContractsRequestDTO, TopContractsResponseDTO
from app.services.contracts import ContractsService

router = APIRouter(prefix="/contracts", tags=["Question 1 - Top Debtors"])

service = ContractsService()


@router.post(
    "/top-debtors",
    response_model=TopContractsResponseDTO,
    summary="Retorna os N maiores devedores sem renegociação",
)
def get_top_debtors(request: TopContractsRequestDTO) -> TopContractsResponseDTO:
    """
    Recebe a lista de contratos em aberto, os já renegociados e o top_n,
    e retorna os IDs dos maiores devedores que ainda não renegociaram.
    """
    return service.get_top_N_open_contracts(
        open_contracts=request.open_contracts,
        renegotiated_contracts=request.renegotiated_contracts,
        top_n=request.top_n,
    )
