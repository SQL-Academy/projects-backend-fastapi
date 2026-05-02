from fastapi import HTTPException

from repositories.users import UserRepository
from schemas import UserCreate
from security import create_access_token, hash_password, verify_password


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, payload: UserCreate):
        if self.repo.get_by_email(payload.email) is not None:
            raise HTTPException(status_code=409, detail="Email already registered")
        return self.repo.create(
            email=payload.email,
            password_hash=hash_password(payload.password),
        )

    def authenticate(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if user is None or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {
            "access_token": create_access_token(user.id),
            "token_type": "bearer",
        }
