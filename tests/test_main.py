from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Hello from CI/CD Pipeline!"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json()["app"] == "python-api-gitops"
