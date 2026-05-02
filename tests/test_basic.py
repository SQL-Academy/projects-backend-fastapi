def test_openapi_available(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == "FastAPI"


def test_tasks_require_auth(client):
    response = client.get("/tasks")
    assert response.status_code == 401


def test_register_login_and_list_tasks(client):
    register = client.post(
        "/auth/register",
        json={"email": "alice@example.com", "password": "qwerty123"},
    )
    assert register.status_code == 201

    login = client.post(
        "/auth/login",
        json={"email": "alice@example.com", "password": "qwerty123"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]

    tasks = client.get("/tasks", headers={"Authorization": f"Bearer {token}"})
    assert tasks.status_code == 200
    assert tasks.json() == []
