from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.tasks import TaskRepository
from schemas import Task, TaskCreate, TaskUpdate
from services.tasks import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)


def get_task_service(
    repo: TaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(repo)


@router.get("", response_model=list[Task])
def get_tasks(
    done: bool | None = None,
    limit: int = 10,
    service: TaskService = Depends(get_task_service),
):
    return service.list(done=done, limit=limit)


@router.get("/{task_id}", response_model=Task)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    return service.get_or_404(task_id)


@router.post("", response_model=Task, status_code=201)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create(payload)


@router.patch("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    return service.update(task_id, payload)


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    service.delete(task_id)
