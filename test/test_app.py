from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_unauthenticated_user_cant_create_todos():   
    department=dict(id=1, department="Test A")
    response = client.post("/deparment", data=department)
    assert response.status_code == 401