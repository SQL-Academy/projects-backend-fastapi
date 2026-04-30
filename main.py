from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

TASKS = [
    {"id": 1, "title": "Купить хлеб", "done": False},
    {"id": 2, "title": "Позвонить врачу", "done": False},
    {"id": 3, "title": "Закончить курс", "done": False},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


@app.get("/tasks")
def get_tasks(done: bool | None = None, limit: int = 10):
    result = TASKS if done is None else [task for task in TASKS if task["done"] == done]
    return result[:limit]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            return task


@app.post("/tasks")
def create_task(payload: TaskCreate):
    new_id = max((task["id"] for task in TASKS), default=0) + 1
    new_task = {"id": new_id, "title": payload.title, "done": payload.done}
    TASKS.append(new_task)
    return new_task
