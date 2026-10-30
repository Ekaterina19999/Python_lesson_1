import os
from yougile_api import YougileApi

BASE_URL = "https://yougile.com"
TOKEN = os.getenv("YOUGILE_TOKEN", "")

api = YougileApi(BASE_URL, TOKEN)


def test_create_project_positive():
    title = "Правильный Проект Тест"
    response = api.create_project(title)

    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert body["id"] is not None


def test_update_project_positive():
    create_resp = api.create_project("Проект под изменение")
    project_id = create_resp.json()["id"]

    new_title = "Успешно Изменено"
    update_resp = api.update_project(project_id, new_title)

    assert update_resp.status_code == 200
    assert update_resp.json()["id"] == project_id


def test_get_project_positive():
    title = "Ищем меня по ID"
    create_resp = api.create_project(title)
    project_id = create_resp.json()["id"]

    get_resp = api.get_project(project_id)

    assert get_resp.status_code == 200
    assert title in get_resp.json()["title"]


def test_create_project_negative_empty_title():
    response = api.create_project("")

    assert response.status_code == 400


def test_update_project_negative_wrong_id():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(fake_id, "Новое имя")

    assert response.status_code == 404


def test_get_project_negative_wrong_id():
    fake_id = "invalid-id-format-123"
    response = api.get_project(fake_id)

    assert response.status_code == 404

