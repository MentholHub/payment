from fastapi.testclient import TestClient

from payment.src.main import app

client = TestClient(app)


def test_ReadRoot():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"key": "value"}
