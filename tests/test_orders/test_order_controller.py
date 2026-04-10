from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestOrdersRouter:
    def test_success(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [1, 2, 3, 4, 5], "n_max": 5},
        )
        assert response.status_code == 200
        assert response.json() == {"total_trips": 3}

    def test_empty_requests(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [], "n_max": 10},
        )
        assert response.status_code == 200
        assert response.json() == {"total_trips": 0}

    def test_single_order(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [100], "n_max": 200},
        )
        assert response.status_code == 200
        assert response.json() == {"total_trips": 1}

    def test_invalid_n_max_zero(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [1, 2, 3], "n_max": 0},
        )
        assert response.status_code == 422

    def test_invalid_n_max_negative(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [1, 2, 3], "n_max": -1},
        )
        assert response.status_code == 422

    def test_invalid_missing_field(self):
        response = client.post(
            "/orders/trip-planning",
            json={"requests": [1, 2, 3]},
        )
        assert response.status_code == 422
