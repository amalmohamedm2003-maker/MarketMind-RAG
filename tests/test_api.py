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

    # Required business contract
    assert "key_insights" in data
    assert "recommendations" in data
    assert "metrics_impact" in data
    assert "confidence_level" in data

    # Optional field
    if "sources" in data:
        assert isinstance(data["sources"], list)
