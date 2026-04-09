from app.dtos.orders import CombineOrdersResponseDTO


class OrdersService:
    def combine_orders(
        self,
        requests: list[int],
        n_max: int,
    ) -> CombineOrdersResponseDTO:
        """
        Calcula o número mínimo de viagens para atender todos os pedidos.

        """
        if not requests:
            return CombineOrdersResponseDTO(total_trips=0)

        total_trips = self._calculate_minimum_trips(requests, n_max)

        return CombineOrdersResponseDTO(total_trips=total_trips)
    

    def _calculate_minimum_trips(self, requests: list[int], n_max: int) -> int:
        """
        Se a soma couber em uma viagem, ambos vão juntos.
        Caso contrário, o maior vai sozinho.
        """
        orders_sorted_by_value = sorted(requests)
        smallest_order_index = 0
        largest_order_index = len(orders_sorted_by_value) - 1
        total_trips = 0

        while smallest_order_index <= largest_order_index:
            smallest_order = orders_sorted_by_value[smallest_order_index]
            largest_order = orders_sorted_by_value[largest_order_index]
            can_combine = smallest_order + largest_order <= n_max

            if can_combine:
                smallest_order_index += 1

            largest_order_index -= 1
            total_trips += 1

        return total_trips
