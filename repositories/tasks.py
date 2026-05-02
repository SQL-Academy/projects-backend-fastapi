from sqlalchemy.orm import Session

import models


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, done: bool | None, limit: int) -> list[models.Task]:
        query = self.db.query(models.Task)
        if done is not None:
            query = query.filter(models.Task.done == done)
        return query.limit(limit).all()

    def get_by_id(self, task_id: int) -> models.Task | None:
        return self.db.get(models.Task, task_id)

    def create(self, title: str, done: bool) -> models.Task:
        task = models.Task(title=title, done=done)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def save(self, task: models.Task) -> models.Task:
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: models.Task) -> None:
        self.db.delete(task)
        self.db.commit()
