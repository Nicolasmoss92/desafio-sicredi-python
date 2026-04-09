from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestContractsRouter:
    def test_sucess(self):
        response = client.post(
            "/contracts/top-debtors",
            json={
                "open_contracts": [{"id": i, "debt": i} for i in range(1, 6)],
                "renegotiated_contracts": [3],
                "top_n": 3,
            },
        )
        assert response.status_code == 200
        assert response.json() == {"top_debtors": [5, 4, 2]}

    def test_invalid_body(self):
        response = client.post(
            "/contracts/top-debtors",
            json={"open_contracts": [], "renegotiated_contracts": [], "top_n": -1},
        )
        assert response.status_code == 422
