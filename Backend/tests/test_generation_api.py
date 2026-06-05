from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_generate_test_cases_api():

    response = client.post(
        "/api/v1/tests/generate",
        json={
            "user_story": "As a user I want login"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["story"] == "As a user I want login"