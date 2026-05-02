from sqlalchemy.orm import Session

import models


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, user_id: int, done: bool | None, limit: int) -> list[models.Task]:
        query = self.db.query(models.Task).filter(models.Task.owner_id == user_id)
        if done is not None:
            query = query.filter(models.Task.done == done)
        return query.limit(limit).all()

    def get_by_id(self, task_id: int, user_id: int) -> models.Task | None:
        return (
            self.db.query(models.Task)
            .filter(models.Task.id == task_id, models.Task.owner_id == user_id)
            .first()
        )

    def create(self, owner_id: int, title: str, done: bool) -> models.Task:
        task = models.Task(owner_id=owner_id, title=title, done=done)
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
