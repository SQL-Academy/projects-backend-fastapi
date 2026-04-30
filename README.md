# TaskList API — учебный проект курса «Backend на FastAPI с нуля»

Сервис «список задач», который мы вместе собираем по ходу [курса на Python Academy](https://python-academy.org/course/backend-fastapi). Каждая версия проекта закреплена тегом — можно склонировать любую и работать с того места.

## Версии

| Тег | Что появилось |
| --- | --- |
| `v0.1-hello-api` | FastAPI + uvicorn, `GET /tasks` с хардкод-данными |

(список будет пополняться по мере выхода уроков)

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
