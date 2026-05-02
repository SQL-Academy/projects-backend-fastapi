from fastapi.testclient import TestClient


def register_and_login(client: TestClient, email: str, password: str) -> dict:
    client.post("/auth/register", json={"email": email, "password": password})
    response = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
