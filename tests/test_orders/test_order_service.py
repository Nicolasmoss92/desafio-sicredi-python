from app.services.orders import OrdersService


class TestOrdersService:
    def setup_method(self):
        self.service = OrdersService()

    def test_success(self):
        result = self.service.combine_orders(requests=[1, 2, 3, 4, 5], n_max=5)
        assert result.total_trips == 3

    def test_empty_requests(self):
        result = self.service.combine_orders(requests=[], n_max=10)
        assert result.total_trips == 0

    def test_single_order(self):
        result = self.service.combine_orders(requests=[100], n_max=200)
        assert result.total_trips == 1

    def test_all_orders_combine(self):
        result = self.service.combine_orders(requests=[1, 2], n_max=10)
        assert result.total_trips == 1

    def test_no_orders_combine(self):
        result = self.service.combine_orders(requests=[3, 4], n_max=5)
        assert result.total_trips == 2

    def test_unsorted_input(self):
        result = self.service.combine_orders(requests=[5, 1, 4, 2, 3], n_max=5)
        assert result.total_trips == 3
