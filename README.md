# TaskList API — учебный проект курса «Backend на FastAPI с нуля»

Сервис «список задач», который мы вместе собираем по ходу [курса на Python Academy](https://python-academy.org/course/backend-fastapi). Каждая версия проекта закреплена тегом — можно склонировать любую и работать с того места.

## Версии

| Тег | Что появилось |
| --- | --- |
| `v0.1-hello-api` | FastAPI + uvicorn, `GET /tasks` с хардкод-данными |
| `v0.1-params` | `GET /tasks/{id}` с path-параметром, фильтр `?done=true` и `?limit=N` через query |
| `v0.1-pydantic` | `POST /tasks` принимает JSON-тело с Pydantic-валидацией |
| `v0.2-responses` | Response-модели через `Task`/`TaskCreate`, статус-код `201` на создание, `404` через `HTTPException` |
| `v0.3-postgres-up` | Postgres 16 в Docker через `docker-compose.yml`, volume для персистентности |
| `v0.3-sqlalchemy-basics` | SQLAlchemy 2.x: модель `Task` в `models.py`, engine + `SessionLocal` в `database.py`, таблица создаётся через `Base.metadata.create_all` |
| `v0.3-depends` | `get_db()` как dependency-with-yield, `GET /tasks` читает из Postgres через `Depends(get_db)`. Таблицы создаются на старте приложения |
| `v0.3-crud-with-db` | `GET /tasks/{id}`, `POST`, `PATCH`, `DELETE` через SQLAlchemy. `TASKS`-список ушёл из кода насовсем |
| `v0.3-alembic` | Миграции через Alembic, две ревизии (создание таблицы + колонка `priority`), `create_all` убран из `main.py` |
| `v0.4-fat-routes` | `routes/tasks.py` через `APIRouter`, Pydantic-схемы вынесены в `schemas.py`, `main.py` похудел до 6 строк |
| `v0.4-services-repositories` | Слои разделены: `routes/`, `services/`, `repositories/`. Бизнес-логика отдельно от SQL |
| `v0.4-config-env` | `pydantic-settings`, `DATABASE_URL` и пароли уехали в `.env`, добавлен `.env.example` |
| `v0.5-password-hashing` | `security.py` с `hash_password` / `verify_password` на bcrypt через passlib |
| `v0.5-register-and-login` | Модель `User`, эндпоинты `/auth/register` и `/auth/login`, миграция для таблицы `users` |
| `v0.5-jwt-tokens` | `/auth/login` возвращает JWT через python-jose, `SECRET_KEY` и `ACCESS_TOKEN_EXPIRE_MINUTES` в env |
| `v0.5-protecting-endpoints` | `dependencies.py` с `get_current_user`, у задач появился `owner_id`, изоляция между пользователями (404 на чужие задачи) |
| `v0.6-pytest-and-test-client` | Первые тесты на pytest + FastAPI `TestClient` в `tests/test_basic.py` |
| `v0.7-test-database-fixture` | Тестовая БД `tasklist_test` и `tests/conftest.py` с фикстурами engine/db_session/client, изоляция через SAVEPOINT |
| `v0.8-what-to-test-in-api` | `tests/helpers.py` с `register_and_login`, тесты разнесены по `test_auth.py` / `test_tasks.py` (golden path, ошибки, инварианты доступа, parametrize) |
| `v0.9-dockerfile-for-fastapi` | `Dockerfile` + `.dockerignore`, сервис `app` добавлен в `docker-compose.yml` с healthcheck для postgres |
| `v1.0-deploy-to-render` | `${PORT}` из окружения, нормализация `DATABASE_URL` через `field_validator` в `config.py` — образ готов к деплою на Render |

## Как запустить локально

```bash
git clone git@github.com:SQL-Academy/projects-backend-fastapi.git
cd projects-backend-fastapi
git checkout v0.1-hello-api

python3 -m venv .venv
source .venv/bin/activate     # на Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload
```

Сервис поднимется на `http://localhost:8000`. Эндпоинты — на `http://localhost:8000/docs`.
