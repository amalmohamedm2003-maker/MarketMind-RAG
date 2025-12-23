from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={"question": "How can I reduce CPA?"}
    )
    assert response.status_code == 200
    assert "sources_used" in response.json()
