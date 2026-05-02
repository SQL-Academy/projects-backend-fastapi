import pytest

from helpers import register_and_login


def test_create_task(client):
    headers = register_and_login(client, "alice@example.com", "qwerty123")

    response = client.post(
        "/tasks",
        json={"title": "Купить молоко", "done": False},
        headers=headers,
    )

    assert response.status_code == 201
    body = response.json()
    assert body["id"] > 0
    assert body["title"] == "Купить молоко"
    assert body["done"] is False


def test_user_cannot_see_other_users_tasks(client):
    bob = register_and_login(client, "bob@example.com", "qwerty123")
    client.post("/tasks", json={"title": "Bob's secret"}, headers=bob)

    alice = register_and_login(client, "alice@example.com", "qwerty123")
    response = client.get("/tasks", headers=alice)

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize("done,expected_count", [(True, 1), (False, 1)])
def test_list_tasks_filter_by_done(client, done, expected_count):
    headers = register_and_login(client, "alice@example.com", "qwerty123")
    client.post("/tasks", json={"title": "Готово", "done": True}, headers=headers)
    client.post("/tasks", json={"title": "В процессе", "done": False}, headers=headers)

    response = client.get("/tasks", params={"done": done}, headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == expected_count
