from sqlalchemy.orm import Session

import models


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> models.User | None:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_by_id(self, user_id: int) -> models.User | None:
        return self.db.get(models.User, user_id)

    def create(self, email: str, password_hash: str) -> models.User:
        user = models.User(email=email, password_hash=password_hash)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
