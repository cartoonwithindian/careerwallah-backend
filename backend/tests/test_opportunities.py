from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_opportunities_list_empty_or_has_data():
    r = client.get("/api/v1/opportunities")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
