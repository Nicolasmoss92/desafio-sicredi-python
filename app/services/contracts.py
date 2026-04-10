from typing import List

from app.dtos.contracts import ContractDTO, TopContractsResponseDTO


class ContractsService:
    def get_top_N_open_contracts(
        self,
        open_contracts: List[ContractDTO],
        renegotiated_contracts: List[int],
        top_n: int,
    ) -> TopContractsResponseDTO:
        """
        Retorna os top_n maiores devedores que ainda não renegociaram.

        """
        if not open_contracts or top_n <= 0:
            return TopContractsResponseDTO(top_debtors=[])

        renegotiated_ids = set(renegotiated_contracts)

        non_renegotiated_contracts = [
            contract
            for contract in open_contracts
            if contract.id not in renegotiated_ids
        ]

        contracts_sorted_by_debt = sorted(
            non_renegotiated_contracts, key=lambda contract: contract.debt, reverse=True
        )

        return TopContractsResponseDTO(
            top_debtors=[contract.id for contract in contracts_sorted_by_debt[:top_n]]
        )
