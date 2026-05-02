from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


class Task(TaskCreate):
    id: int
    priority: int | None = None
