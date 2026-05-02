from fastapi import HTTPException

from repositories.tasks import TaskRepository
from schemas import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def list(self, user_id: int, done: bool | None, limit: int):
        return self.repo.list(user_id=user_id, done=done, limit=limit)

    def get_or_404(self, task_id: int, user_id: int):
        task = self.repo.get_by_id(task_id, user_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create(self, payload: TaskCreate, user_id: int):
        return self.repo.create(
            owner_id=user_id,
            title=payload.title,
            done=payload.done,
        )

    def update(self, task_id: int, payload: TaskUpdate, user_id: int):
        task = self.get_or_404(task_id, user_id)
        if payload.title is not None:
            task.title = payload.title
        if payload.done is not None:
            task.done = payload.done
        return self.repo.save(task)

    def delete(self, task_id: int, user_id: int) -> None:
        task = self.get_or_404(task_id, user_id)
        self.repo.delete(task)
