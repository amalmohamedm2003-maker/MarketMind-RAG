from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={"question": "How to reduce CPA?"}
    )

    assert response.status_code == 200

    data = response.json()

    # Business-grade API contract
    assert "key_insights" in data
    assert "recommendations" in data
    assert "metrics_impact" in data
    assert "confidence_level" in data
    assert "sources" in data
