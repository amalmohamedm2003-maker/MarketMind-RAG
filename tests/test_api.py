from fastapi.testclient import TestClient
from backend.api.main import app

def test_api_health():
    client = TestClient(app)
    r = client.get("/docs")
    assert r.status_code == 200
