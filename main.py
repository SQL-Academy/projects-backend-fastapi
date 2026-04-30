from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db

Base.metadata.create_all(engine)

app = FastAPI()

TASKS = [
    {"id": 1, "title": "Купить хлеб", "done": False},
    {"id": 2, "title": "Позвонить врачу", "done": False},
    {"id": 3, "title": "Закончить курс", "done": False},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


@app.get("/tasks", response_model=list[Task])
def get_tasks(
    done: bool | None = None,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(models.Task)
    if done is not None:
        query = query.filter(models.Task.done == done)
    return query.limit(limit).all()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    new_id = max((task["id"] for task in TASKS), default=0) + 1
    new_task = {"id": new_id, "title": payload.title, "done": payload.done}
    TASKS.append(new_task)
    return new_task
