from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.users import UserRepository
from schemas import TokenOut, UserCreate, UserOut
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_auth_service(
    repo: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(repo)


@router.post("/register", response_model=UserOut, status_code=201)
def register(
    payload: UserCreate,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(payload)


@router.post("/login", response_model=TokenOut)
def login(
    payload: UserCreate,
    service: AuthService = Depends(get_auth_service),
):
    return service.authenticate(payload.email, payload.password)
