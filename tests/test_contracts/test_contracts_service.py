from fastapi.testclient import TestClient

from app.dtos.contracts import ContractDTO
from app.main import app
from app.services.contracts import ContractsService

client = TestClient(app)
service = ContractsService()


class TestContractsService:
    def test_returns_top_debtors_excluding_renegotiated(self):
        contracts = [ContractDTO(id=i, debt=i) for i in range(1, 6)]
        result = service.get_top_N_open_contracts(contracts, [3], 3)
        assert result.top_debtors == [5, 4, 2]

    def test_returns_empty_list_when_no_contracts(self):
        result = service.get_top_N_open_contracts([], [], 3)
        assert result.top_debtors == []

    def test_returns_all_when_top_n_exceeds_list_size(self):
        contracts = [ContractDTO(id=1, debt=100), ContractDTO(id=2, debt=50)]
        result = service.get_top_N_open_contracts(contracts, [], 10)
        assert result.top_debtors == [1, 2]

    def test_returns_empty_when_all_contracts_renegotiated(self):
        contracts = [ContractDTO(id=1, debt=100), ContractDTO(id=2, debt=50)]
        result = service.get_top_N_open_contracts(contracts, [1, 2], 2)
        assert result.top_debtors == []

    def test_returns_empty_when_top_n_is_zero(self):
        contracts = [ContractDTO(id=1, debt=100)]
        result = service.get_top_N_open_contracts(contracts, [], 0)
        assert result.top_debtors == []
