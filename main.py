from fastapi import FastAPI

app = FastAPI()

TASKS = [
    {"id": 1, "title": "Купить хлеб", "done": False},
    {"id": 2, "title": "Позвонить врачу", "done": False},
    {"id": 3, "title": "Закончить курс", "done": False},
]


@app.get("/tasks")
def get_tasks(done: bool | None = None, limit: int = 10):
    result = TASKS if done is None else [task for task in TASKS if task["done"] == done]
    return result[:limit]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            return task
