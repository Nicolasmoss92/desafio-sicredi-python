from fastapi import APIRouter

from app.dtos.orders import CombineOrdersRequestDTO, CombineOrdersResponseDTO
from app.services.orders import OrdersService

router = APIRouter(prefix="/orders", tags=["Questão 2 - Quantidade mínima de viagens"])

service = OrdersService()


@router.post(
    "/trip-planning",
    response_model=CombineOrdersResponseDTO,
    summary="Calcula o número mínimo de viagens para atender todos os pedidos",
)
def combine_orders(request: CombineOrdersRequestDTO) -> CombineOrdersResponseDTO:
    """
    Recebe uma lista de pedidos e o valor máximo por viagem,
    e retorna o número mínimo de viagens necessárias.
    """
    return service.combine_orders(
        requests=request.requests,
        n_max=request.n_max,
    )