from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

# Create a fresh test DB (in-memory for simplicity)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "secretpass"
    }

    response = client.post("/api/users/", json=user_data)

    print("RESPONSE:", response.status_code, response.json())  # 👈 Add this line

    assert response.status_code == 200
    result = response.json()
    assert result["username"] == user_data["username"]
    assert result["email"] == user_data["email"]
    assert "created_at" in result
