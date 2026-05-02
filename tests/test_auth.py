def test_register_duplicate_email_409(client):
    payload = {"email": "alice@example.com", "password": "qwerty123"}
    client.post("/auth/register", json=payload)

    response = client.post("/auth/register", json=payload)

    assert response.status_code == 409


def test_login_wrong_password_401(client):
    client.post(
        "/auth/register",
        json={"email": "alice@example.com", "password": "qwerty123"},
    )

    response = client.post(
        "/auth/login",
        json={"email": "alice@example.com", "password": "wrong-password"},
    )

    assert response.status_code == 401
